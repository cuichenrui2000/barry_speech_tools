#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from tqdm import tqdm

# 读取原始文件内容并显示进度条
with open("data.list", "r") as file:
    lines = [line.strip() for line in tqdm(file, desc="Reading Data", unit=" lines")]

# 随机抽取 20000 行作为测试数据
test_lines = random.sample(lines, 20000)

# 将剩余的行作为训练数据
train_lines = []
for line in tqdm(lines, desc="Filtering Train Data", unit=" lines"):
    if line not in test_lines:
        train_lines.append(line)

# 将训练数据写入文件
with open("data_train.list", "w") as train_file:
    for line in tqdm(train_lines, desc="Writing Train Data", unit=" lines"):
        train_file.write(line + "\n")

# 将测试数据写入文件
with open("data_test.list", "w") as test_file:
    for line in tqdm(test_lines, desc="Writing Test Data", unit=" lines"):
        test_file.write(line + "\n")
