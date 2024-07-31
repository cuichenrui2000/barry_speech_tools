# 2024_02_04
# 数据后处理脚本，负责将文本规范化

import argparse
from tn.chinese.normalizer import Normalizer

parser = argparse.ArgumentParser()
parser.add_argument('--raw_file_path', type=str, help="需要进行后处理的文件路径")
parser.add_argument('--norm_file_path', type=str, help="处理后的文件路径")
args = parser.parse_args()

raw_file_path = args.raw_file_path
norm_file_path = args.norm_file_path

normalizer = Normalizer()

with open(raw_file_path, "r") as raw_file, open(norm_file_path, "w") as norm_file:
    for line in raw_file:

        parts = line.strip().split("\t")
        norm_text = normalizer.normalize(parts[1])
        norm_file.write(f"{parts[0][-30:]}\t{norm_text}\n")