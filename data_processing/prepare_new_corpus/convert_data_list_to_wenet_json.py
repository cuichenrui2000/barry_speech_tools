#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from tqdm import tqdm
import os
import string
import re

def remove_punctuation(input_string):
    """去除所有标点符号"""
    translation_table = str.maketrans("", "", string.punctuation + "，。、；：！？（）【】『』“”《》［］｛｝﹙﹚﹛﹜﹝﹞〔〕〈〉")
    no_punct = input_string.translate(translation_table)
    return no_punct

filename_list = ["data.list", "data_test.list", "data_train.list"]

for filename in filename_list:
    # 读取原始文件，转换格式，写入新文件
    with open(filename, "r", encoding="utf-8") as f_in, \
        open(filename.replace("data", "wenet"), "w", encoding="utf-8") as f_out:
        lines = f_in.readlines()
        total_lines = len(lines)
        for line in tqdm(lines, desc=f"Processing {filename}", unit=" lines"):
            
            # duration 字段暂时用不到
            path, text, _ = line.strip().split("\t")
            text = remove_punctuation(text)

            data = {
                "key": path,
                "wav": path,
                "txt": text
            }
            json.dump(data, f_out, ensure_ascii=False)
            f_out.write('\n')
