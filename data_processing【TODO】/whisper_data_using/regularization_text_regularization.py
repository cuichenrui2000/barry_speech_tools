import re
import json
import jsonlines
from tqdm import tqdm

import jiwer
from MyEnglishTextNormalizer import EnglishTextNormalizer

def normalize_text(text):
    
    text = text.strip()
    alpha = "'-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    normalized_text = ""
    
    fill_blanks = False
    # 处理每个字符
    for i in range(len(text)):
        # 如果是空格
        if text[i] == " ":
            # 如果空格左右有一侧是英文字母则保留
            # 空格左边右边一定有字符，[i-1][i+1]不用考虑越界
            if text[i-1] in alpha or text[i+1] in alpha:
                normalized_text += text[i]
        
        # 如果 i 不是最后一个字符；i+1 不是空格；i 和 i+1 一英一中
        elif (i+1 < len(text)) and (text[i+1] != " ") and ((text[i] in alpha and text[i+1] not in alpha) or (text[i+1] in alpha and text[i] not in alpha)):
            fill_blanks = True
            normalized_text += text[i]
            normalized_text += " "
        
        # 如果非空格或英文字母，不做改变
        else:
            normalized_text += text[i]

    if fill_blanks:
        print(f"原始文本：{text}")
        print(f"补空格后：{normalized_text}")
            
    return normalized_text

normalizer = EnglishTextNormalizer()

with jsonlines.open("train_all_new_checked_without_8k_regularization_3.jsonl", mode="w") as output_file, open("train_all_new_checked_without_8k_regularization_2.jsonl", 'r') as f:
    lines = f.readlines()
    for line in tqdm(lines, desc="Processing", unit="lines"):
        data = json.loads(line)
        audio_path = data['audio']['path']
        sentence = data['sentence']
        duration = data['duration']
        language = data['language']
        
        sentence1 = normalizer(sentence)
        sentence2 = normalize_text(sentence1)
        
        result_json = {"audio": {"path": audio_path}, "sentence": sentence2, "language": language, "duration": duration}
        output_file.write(result_json)