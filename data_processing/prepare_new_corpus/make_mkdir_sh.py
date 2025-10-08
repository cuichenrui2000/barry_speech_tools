#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# 用于存储所有.wav文件的前缀路径
prefixes = set()

# 打开文件并处理数据
with open("copy.sh", "r") as infile:
    for line in infile:
        # 按空格分割行
        parts = line.strip().split(" ")
        # 获取新音频路径
        audio_path = parts[2]
        if audio_path.endswith(".wav"):
            # 提取前缀路径并添加到集合中
            prefix = os.path.dirname(audio_path)
            prefixes.add(prefix)

# 将前缀路径写入新文件
with open("mkdir.sh", "w") as outfile:
    for prefix in prefixes:
        outfile.write(f"mkdir -p {prefix}\n")
