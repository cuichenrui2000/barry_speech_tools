#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from tqdm import tqdm

# 定义目标目录路径
target_dir = 'prefix_path_of_all_data'

# 遍历目录并找出所有后缀为 .wav 的文件
wav_files = []
for root, dirs, files in os.walk(target_dir):
    for file in tqdm(files, desc='Searching .wav files'):
        if file.endswith('.wav'):
            wav_files.append(os.path.join(root, file))

# 将所有音频绝对路径输出到文件
with open('all_wavpath.txt', 'w') as f:
    for wav_file in tqdm(wav_files, desc='Writing paths to file'):
        f.write(wav_file + '\n')
