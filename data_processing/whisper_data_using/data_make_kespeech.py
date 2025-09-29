#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonlines
from tqdm import tqdm
import os

train_folder_list = ["train_phase1", "train_phase2", "dev_phase1", "dev_phase2"]
wavscp_filename_example = "your_kespeech_path/<need_to_filled>/wav.scp"
text_filename_example = "your_kespeech_path/<need_to_filled>/text"
train_jsonl_filename = "your_result_jsonl_path"

data_dict = {}
all_train_items = 0
all_train_duration = 0

for train_folder in train_folder_list:
    
    wavscp_filename = wavscp_filename_example.replace("<need_to_filled>", train_folder)
    text_filename = text_filename_example.replace("<need_to_filled>", train_folder)
    
    # 处理 wavscp 文件
    with open(wavscp_filename, 'r') as wavscp_file:
        for line in tqdm(wavscp_file):
            # 使用空格分割每一行的内容
            key, audio_path = line.strip().split(' ')
            audio_path = "your_kespeech_path/" + audio_path
            if os.path.exists(audio_path):
                data_dict[key] = [audio_path]
            else:
                print(f"错误路径：{audio_path}")

    # 处理 text 文件           
    with open(text_filename, 'r') as text_file:
        for line in tqdm(text_file):
            # 使用空格分割每一行的内容
            # 鲁棒解决音频无文本问题
            if " " in line:
                key, text = line.strip().split(' ', 1)
            else:
                key, text = line.strip(), ""
                print(f"无文本音频：{line}")
                # 无文本音频是否进行保留
                # continue
            
            # 这个数据集有特殊字符，进行去除
            text = text.replace("<SPOKEN_NOISE>", "")
            data_dict[key].append(text)

# 数据写入新文件
with jsonlines.open(train_jsonl_filename, mode="w") as train_jsonl_file:
            
    for key, value in tqdm(data_dict.items()):
        
        audio_path, text = value
        
        # 巧妙计算音频时长
        filesize = os.path.getsize(audio_path)
        duration = float(filesize-44) / 2 / 16000
        duration = round(duration, 2)
        
        result_json = {"audio": {"path": audio_path}, "sentence": text, "language": "chinese", "duration": duration}
        
        train_jsonl_file.write(result_json)
        all_train_items += 1
        all_train_duration += duration

print(f"all_train_items = {all_train_items}")
print(f"all_train_duration = {round(all_train_duration / 3600, 2)}h")
