#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonlines
from tqdm import tqdm

# 大写字母字典
upper_dict = {
    "a": "A", 
    "b": "B",
    "c": "C", 
    "d": "D", 
    "e": "E", 
    "f": "F", 
    "g": "G",
    "h": "H", 
    "i": "I", 
    "j": "J", 
    "k": "K", 
    "l": "L",
    "m": "M", 
    "n": "N", 
    "o": "O", 
    "p": "P", 
    "q": "Q",
    "r": "R", 
    "s": "S", 
    "t": "T", 
    "u": "U", 
    "v": "V",
    "w": "W", 
    "x": "X", 
    "y": "Y", 
    "z": "Z"
}
    
# 中英混数据前缀
zh_en_list = ["zh_en_prefix_path1", 
              "zh_en_prefix_path2", 
              "zh_en_prefix_path3"]

# 正则化文本 dict
norm_dict = {}
# 加载已正则化后的数据文本
for file_path in ["normed_test1.list", "normed_test2.list"]:
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in tqdm(lines, desc="Processing Reading", unit="lines"):
            data = json.loads(line.strip())
            wav = data["wav"]
            text = data["txt"]
            norm_dict[wav] = text

# 文件路径
raw_file_path = "your_raw_file_path"
new_file_path = "your_new_file_path"
others_file_path = "your_others_file_path"

get_num = 0
get_duration = 0
not_get_num = 0
not_get_duration = 0
ch_en_num = 0
ch_en_duration = 0
special_num = 0
special_duration = 0

# 逐行读取文件
with open(raw_file_path, "r") as file, jsonlines.open(new_file_path, "w") as wenet_file, jsonlines.open(others_file_path, "w") as others_file:
    lines = file.readlines()
    for line in tqdm(lines, desc="Processing Checking", unit="lines"):
        
        # 解析 json 数据
        data = json.loads(line.strip())
        key = data["key"]
        wav = data["wav"]
        text = data["txt"]
        
        # 1. 中英混数据去除
        pass_data = False
        for i in zh_en_list:
            if i in wav:
                pass_data = True
        # 去除数据
        if pass_data:
            ch_en_num += 1
            # ch_en_duration += duration
            continue
                
        # 2. 去除所有【含两个单词以上】的句子，单字母不算单词【逻辑不严谨，bug 未修复】
        text_words = text.split(" ")
        word_num = 0
        for text_word in text_words:
            letter_num = 0
            for text_letter in text_word:
                if text_letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    letter_num += 1
                    if letter_num == 2:
                        word_num += 1
                        continue
        # 去除数据
        if word_num >= 2:
            print(line)
            special_num += 1
            # special_duration += duration
            continue
        
        # 3. 执行文本正则化替换 text
        text_new = norm_dict.get(wav, "NOT_EXISTES")
        
        # 3.5 英文字母小写转换为大写
        for i in upper_dict.keys():
            text_new = text_new.replace(i, upper_dict[i])
        
        # 4. 无条件去除所有空格
        text_new = text_new.replace(" ", "")
        
        # 若命中，写入 text_new
        if text_new != "NOT_EXISTES":
            get_num += 1
            # get_duration += duration
            result_json = {"key": key, "wav": wav, "txt": text_new}
            wenet_file.write(result_json)
            
        # 若未命中，写入 text
        else:
            not_get_num += 1
            # not_get_duration += duration
            result_json = {"key": key, "wav": wav, "txt": text}
            others_file.write(result_json)

# 打印变量
print("GET Numbers:", get_num)
print("GET Duration:", round(get_duration / 3600, 2), "h")
print("NOT GET Numbers:", not_get_num)
print("NOT GET Duration:", round(not_get_duration / 3600, 2), "h")
print("ZH EN Numbers:", ch_en_num)
print("ZH EN Duration:", round(ch_en_duration / 3600, 2), "h")
print("Special Numbers:", special_num)
print("Special Duration:", round(special_duration / 3600, 2), "h")
