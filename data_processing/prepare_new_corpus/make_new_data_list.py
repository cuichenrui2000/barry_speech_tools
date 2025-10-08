#!/usr/bin/python
# -*- coding: utf-8 -*-

from tqdm import tqdm
import os

# 打开原始文件和输出文件
with open('your_wavpath_file', 'r') as f_paths, open('data.list', 'w') as f_output:
    # 使用 tqdm 包装路径读取以显示进度条
    for line in tqdm(f_paths, desc='Processing paths'):
        # 移除换行符并提取路径
        raw_path = line.strip()
        audio_path = raw_path.replace("your_old_prefix_path", "your_new_prefix_path")

        # 巧妙读取音频时长，数据还未迁移完，因此使用原始路径
        filesize = os.path.getsize(raw_path)
        duration = float(filesize-44) / 2 / 16000
        duration = round(duration, 2)

        # 将路径的后缀改为 .txt，找到音频对应文本
        text_path = raw_path.replace('.wav', '.txt')
        # 读取 .txt 文件的内容并移除换行符
        with open(text_path, 'r') as f_text:
            text_content = f_text.read().strip()
        # 将路径和文本内容以制表符分隔写入输出文件
        f_output.write(f"{audio_path}\t{text_content}\t{duration}\n")