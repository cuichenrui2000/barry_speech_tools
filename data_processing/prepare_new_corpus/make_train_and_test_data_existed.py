#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tqdm import tqdm

# 读取已拆分的测试集
moved_filenames = set()
with open("data_test_old.list", "r") as moved_file:
    for line in moved_file:
        moved_filenames.add(line.strip().split("\t")[0])

# 打开全部数据文件
with open("data.list", "r") as original_file:
    lines = original_file.readlines()

# 将测试集和训练集进行拆分
train_count = 0
test_count = 0
with open("data_train.list", "w") as train_file, open("data_test.list", "w") as test_file:
    for line in tqdm(lines, desc="Processing", unit=" lines"):
        parts = line.strip().split("\t")
        filename = parts[0]
        if filename in moved_filenames:
            test_file.write(line)
            test_count += 1
        else:
            train_file.write(line)
            train_count += 1

# 打印新文件的行数
print("data_train.list 行数:", train_count)
print("data_test.list 行数:", test_count)
