#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from tqdm import tqdm

# 文件路径
file_path = "your_result_jsonl_path"

# 初始化统计变量
total_files = 0
correct_files = 0
incorrect_files = 0
total_duration = 0
correct_duration = 0
incorrect_duration = 0

# 逐行读取文件
with open(file_path, "r") as file:
    lines = file.readlines()
    # 使用tqdm显示进度条
    for line in tqdm(lines, desc="Processing lines", unit="lines"):
        # 解析每一行的JSON数据
        data = json.loads(line.strip())
        audio_path = data["audio"]["path"]
        duration = data["duration"]
        
        # 更新总文件数和总时长
        total_files += 1
        total_duration += duration
        
        # 检查文件是否存在
        if os.path.exists(audio_path):
            correct_files += 1
            correct_duration += duration
        else:
            incorrect_files += 1
            incorrect_duration += duration

# 输出结果
print("Total files:", total_files)
print("Correct files:", correct_files)
print("Incorrect files:", incorrect_files)
print("Total duration:", total_duration)
print("Correct duration:", correct_duration)
print("Incorrect duration:", incorrect_duration)
