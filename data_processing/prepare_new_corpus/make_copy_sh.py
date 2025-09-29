#!/usr/bin/python
# -*- coding: utf-8 -*-

# 打开原始文件和输出文件
with open('your_wavpath_file', 'r') as f_original, open('copy.sh', 'w') as f_output:
    # 逐行读取原始文件内容
    for line in f_original:
        # 去除末尾的换行符并生成迁移后路径
        raw_path = line.strip()
        audio_path = raw_path.replace("your_old_prefix_path", "your_new_prefix_path")

        # 写入原始路径和新路径到输出文件
        f_output.write(f"cp {raw_path} {audio_path}\n")
