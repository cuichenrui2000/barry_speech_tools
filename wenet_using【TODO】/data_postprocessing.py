#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from tn.chinese.normalizer import Normalizer

parser = argparse.ArgumentParser()
parser.add_argument('--raw_file_path', type=str, help="输入文件路径")
parser.add_argument('--norm_file_path', type=str, help="输出文件路径")
args = parser.parse_args()

raw_file_path = args.raw_file_path
norm_file_path = args.norm_file_path

normalizer = Normalizer()

with open(raw_file_path, "r") as raw_file, open(norm_file_path, "w") as norm_file:
    for line in raw_file:
        parts = line.strip().split("\t")
        
        # 若该文件存在识别结果，则对识别结果进行文本正则化
        if len(parts) >= 2:
            norm_text = normalizer.normalize(parts[1])
            norm_file.write(f"{parts[0]}\t{norm_text}\n")
            
        # 若该文件不存在识别结果，则识别结果仍然为空
        else:
            norm_file.write(f"{parts[0]}\t\n")
