import re
import json
import jsonlines
from tqdm import tqdm

quanjiao_dict = {
    "０": "0",
    "１": "1",
    "２": "2",
    "３": "3",
    "４": "4",
    "５": "5",
    "６": "6",
    "７": "7",
    "８": "8",
    "９": "9",
    "Ａ": "A",
    "Ｂ": "B",
    "Ｃ": "C",
    "Ｄ": "D",
    "Ｅ": "E",
    "Ｆ": "F",
    "Ｇ": "G",
    "Ｈ": "H",
    "Ｉ": "I",
    "Ｊ": "J",
    "Ｋ": "K",
    "Ｌ": "L",
    "Ｍ": "M",
    "Ｎ": "N",
    "Ｏ": "O",
    "Ｐ": "P",
    "Ｑ": "Q",
    "Ｒ": "R",
    "Ｓ": "S",
    "Ｔ": "T",
    "Ｕ": "U",
    "Ｖ": "V",
    "Ｗ": "W",
    "Ｘ": "X",
    "Ｙ": "Y",
    "Ｚ": "Z",
    "ａ": "a",
    "ｂ": "b",
    "ｃ": "c",
    "ｄ": "d",
    "ｅ": "e",
    "ｆ": "f",
    "ｇ": "g",
    "ｈ": "h",
    "ｉ": "i",
    "ｊ": "j",
    "ｋ": "k",
    "ｌ": "l",
    "ｍ": "m",
    "ｎ": "n",
    "ｏ": "o",
    "ｐ": "p",
    "ｑ": "q",
    "ｒ": "r",
    "ｓ": "s",
    "ｔ": "t",
    "ｕ": "u",
    "ｖ": "v",
    "ｗ": "w",
    "ｘ": "x",
    "ｙ": "y",
    "ｚ": "z"
}

# 定义文件路径
file_path = "/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/2_special_characters.txt"

# 初始化一个空列表
special_characters_list = []
special_characters_path = 
# 打开文件并读取每一行
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 有的特殊字符就是空白，不能直接strip()
        line = line.replace("\n", "")
        special_characters_list.append(line)

with jsonlines.open("train_all_new_checked_without_8k_regularization_2.jsonl", mode="w") as output_file, open("train_all_new_checked_without_8k_regularization.jsonl", 'r') as f:
    lines = f.readlines()
    for line in tqdm(lines, desc="Processing", unit="lines"):
        pass_data = False
        data = json.loads(line)
        audio_path = data['audio']['path']
        sentence = data['sentence']
        duration = data['duration']
        language = data['language']
        
        sentence = sentence.strip()
        # 去除几个中文标点
        for i in ["。", "？", "﹐", "，"]:
            sentence = sentence.replace(i, "")
        # 全角字符转化为半角字符
        for i in quanjiao_dict.keys():
            sentence = sentence.replace(i, quanjiao_dict[i])
        
        result_json = {"audio": {"path": audio_path}, "sentence": sentence, "language": language, "duration": duration}
        
        for i in special_characters_list:
            # 文本中有特殊字符
            if i in sentence:
                print(result_json)
                pass_data = True
                break
            
        if not pass_data:
            output_file.write(result_json)
