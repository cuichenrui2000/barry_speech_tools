#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonlines
from tqdm import tqdm
import os

data_dict = {}

raw_result_file_items = 0
raw_result_file_duration = 0

raw_list_filename = "your_aishell2_path/wav.scp"
raw_text_filename = "your_aishell2_path/trans.txt"
raw_result_filename = "your_result_jsonl_path"

# 处理 list 文件
with open(raw_list_filename, 'r') as raw_list_file:
    for line in tqdm(raw_list_file, desc="Processing List", unit="lines"):
        key, audio_path = line.strip().split('\t')
        # 补充音频路径前缀
        audio_path = os.path.join("your_aishell2_path", audio_path)
        if os.path.exists(audio_path):
            data_dict[key] = [audio_path]
        else:
            print(f"错误路径：{audio_path}")

# 处理 text 文件           
with open(raw_text_filename, 'r') as raw_text_file:
    for line in tqdm(raw_text_file, desc="Processing Text", unit="lines"):
        # 使用 \t 分割每一行的内容
        # 鲁棒解决音频无文本问题
        if "\t" in line:
            key, text = line.strip().split('\t')
        else:
            key, text = line.strip(), ""
            print(f"无文本音频：{line}")
            # 无文本音频是否进行保留
            # continue
        
        data_dict[key].append(text)

# 数据写入新文件
with jsonlines.open(raw_result_filename, mode="w") as raw_result_file:
    for key, value in tqdm(data_dict.items(), desc="Processing Result", unit="lines"):
        audio_path, text = value
        
        # 巧妙计算音频时长
        filesize = os.path.getsize(audio_path)
        duration = float(filesize-44) / 2 / 16000
        duration = round(duration, 2)
        
        result_json = {"audio": {"path": audio_path}, "sentence": text, "language": "chinese", "duration": duration}
        
        # 写入文件
        raw_result_file.write(result_json)
        raw_result_file_items += 1
        raw_result_file_duration += duration

print(raw_result_filename)
print(f"items = {raw_result_file_items}")
print(f"duration = {round(raw_result_file_duration / 3600, 2)}h")
    