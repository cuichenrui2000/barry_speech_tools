#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from tqdm import tqdm

def check_file_existence(file_path):
    """检查文件是否存在，不存在则打印路径"""
    if not os.path.exists(file_path):
        print(f"文件不存在：{file_path}")
        return False
    return True

def count_files(file_path):
    """读取文件，检查每一行的路径是否存在，统计总文件数和存在的文件数"""
    total_files = 0
    correct_files = 0
    total_duration = 0
    with open(file_path, 'r') as file:
        lines = file.readlines()
        total_files = len(lines)
        for line in tqdm(lines, desc="检查文件存在性"):
            path = line.strip().split('\t')[0]
            if check_file_existence(path):
                correct_files += 1
                total_duration += float(line.strip().split('\t')[2])
    return total_files, correct_files, total_duration

if __name__ == "__main__":
    input_file_path = "your_file_path_list"
    total_files, correct_files, total_duration = count_files(input_file_path)
    print(f"总文件数：{total_files}")
    print(f"正确文件数：{correct_files}")
    print(f"总时长：{round(total_duration / 3600, 2)}h")
