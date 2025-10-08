#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from tqdm import tqdm

text_dict = set()

with open("your_data_list_path", 'r') as f:
    lines = f.readlines()
    for line in tqdm(lines, desc="Processing", unit="lines"):
        data = json.loads(line)
        sentence = data['txt']

        for i in sentence:
            text_dict.add(i)

result = list(text_dict)

# 排序便于查看，还可以根据排序后的结果一眼看出特殊字符，并重新进行数据清洗
result.sort()

# 添加 wenet 字典的特殊 token
final_result = ["<blank>", "<unk>"] + result + ["<sos>", "<eos>"]

for i in range(len(final_result)):
    print(final_result[i] + " " + str(i))
