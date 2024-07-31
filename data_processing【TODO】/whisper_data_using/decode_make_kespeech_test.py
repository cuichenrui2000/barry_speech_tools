#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonlines
from tqdm import tqdm
import os

wavscp_filename = "/ofs/speechssd/datasets/opensource_data/ASR/KeSpeech/KeSpeech/Tasks/ASR/test/wav.scp"
text_filename = "/ofs/speechssd/datasets/opensource_data/ASR/KeSpeech/KeSpeech/Tasks/ASR/test/text"
dialect_filename = "/ofs/speechssd/datasets/opensource_data/ASR/KeSpeech/KeSpeech/Tasks/ASR/test/utt2subdialect"

mandarin_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/00_mandarin/mandarin.jsonl"
bj_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/01_bj/bj.jsonl"
xn_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/02_xn/xn.jsonl"
zy_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/03_zy/zy.jsonl"
db_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/04_db/db.jsonl"
ly_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/05_ly/ly.jsonl"
jh_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/06_jh/jh.jsonl"
jl07_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/07_jl/jl.jsonl"
jl08_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/08_jl/jl.jsonl"
all_test_filename = "/nfs/volume-225-14/cuichenrui/dataset/13_kespeech/kespeech.jsonl"

data_dict = {}

# 处理 wavscp 文件
with open(wavscp_filename, 'r') as wavscp_file:
    for line in tqdm(wavscp_file):
        # 使用空格分割每一行的内容
        key, audio_path = line.strip().split(' ')
        audio_path = "/ofs/speechssd/datasets/opensource_data/ASR/KeSpeech/KeSpeech/" + audio_path
        if os.path.exists(audio_path):
            data_dict[key] = [audio_path]
        else:
            print(f"错误路径：{audio_path}")

# 处理 text 文件           
with open(text_filename, 'r') as text_file:
    for line in tqdm(text_file):
        # 使用空格分割每一行的内容
        key, text = line.strip().split(' ')
        text = text.replace("<SPOKEN_NOISE>", "")
        data_dict[key].append(text)

# 处理 dialect 文件        
with open(dialect_filename, 'r') as dialect_file:
    for line in tqdm(dialect_file):
        # 使用空格分割每一行的内容
        key, dialect = line.strip().split(' ')
        data_dict[key].append(dialect)

# 初始化统计量
mandarin_items = 0
mandarin_duration = 0
bj_items = 0
bj_duration = 0
xn_items = 0
xn_duration = 0
zy_items = 0
zy_duration = 0
db_items = 0
db_duration = 0
ly_items = 0
ly_duration = 0
jh_items = 0
jh_duration = 0
jl07_items = 0
jl07_duration = 0
jl08_items = 0
jl08_duration = 0
all_test_items = 0
all_test_duration = 0

# 数据写入新文件
with jsonlines.open(mandarin_filename, mode="w") as mandarin_file, \
        jsonlines.open(bj_filename, mode="w") as bj_file, \
        jsonlines.open(xn_filename, mode="w") as xn_file, \
        jsonlines.open(zy_filename, mode="w") as zy_file, \
        jsonlines.open(db_filename, mode="w") as db_file, \
        jsonlines.open(ly_filename, mode="w") as ly_file, \
        jsonlines.open(jh_filename, mode="w") as jh_file, \
        jsonlines.open(jl07_filename, mode="w") as jl07_file, \
        jsonlines.open(jl08_filename, mode="w") as jl08_file, \
        jsonlines.open(all_test_filename, mode="w") as all_test_file:
            
    for key, value in tqdm(data_dict.items()):
        
        audio_path, text, dialect = value
        
        # 巧妙计算音频时长
        filesize = os.path.getsize(audio_path)
        duration = float(filesize-44) / 2 / 16000
        duration = round(duration, 2)
        
        result_json = {"audio": {"path": audio_path}, "sentence": text, "language": "chinese", "duration": duration}
        
        # 子文件写入
        if dialect == "Mandarin":
            mandarin_file.write(result_json)
            mandarin_items += 1
            mandarin_duration += duration
        elif dialect == "Beijing":
            bj_file.write(result_json)
            bj_items += 1
            bj_duration += duration
        elif dialect == "Southwestern":
            xn_file.write(result_json)
            xn_items += 1
            xn_duration += duration
        elif dialect == "Zhongyuan":
            zy_file.write(result_json)
            zy_items += 1
            zy_duration += duration
        elif dialect == "Northeastern":
            db_file.write(result_json)
            db_items += 1
            db_duration += duration
        elif dialect == "Lan-Yin":
            ly_file.write(result_json)
            ly_items += 1
            ly_duration += duration
        elif dialect == "Jiang-Huai":
            jh_file.write(result_json)
            jh_items += 1
            jh_duration += duration
        elif dialect == "Ji-Lu":
            jl07_file.write(result_json)
            jl07_items += 1
            jl07_duration += duration
        elif dialect == "Jiao-Liao":
            jl08_file.write(result_json)
            jl08_items += 1
            jl08_duration += duration
        else:
            print(f"错误标签：{result_json}")
            
        # 总文件写入
        all_test_file.write(result_json)
        all_test_items += 1
        all_test_duration += duration

print(f"mandarin_items = {mandarin_items}")
print(f"mandarin_duration = {round(mandarin_duration / 3600, 2)}h")

print(f"bj_items = {bj_items}")
print(f"bj_duration = {round(bj_duration / 3600, 2)}h")

print(f"xn_items = {xn_items}")
print(f"xn_duration = {round(xn_duration / 3600, 2)}h")

print(f"zy_items = {zy_items}")
print(f"zy_duration = {round(zy_duration / 3600, 2)}h")

print(f"db_items = {db_items}")
print(f"db_duration = {round(db_duration / 3600, 2)}h")

print(f"ly_items = {ly_items}")
print(f"ly_duration = {round(ly_duration / 3600, 2)}h")

print(f"jh_items = {jh_items}")
print(f"jh_duration = {round(jh_duration / 3600, 2)}h")

print(f"jl07_items = {jl07_items}")
print(f"jl07_duration = {round(jl07_duration / 3600, 2)}h")

print(f"jl08_items = {jl08_items}")
print(f"jl08_duration = {round(jl08_duration / 3600, 2)}h")

print(f"all_test_items = {all_test_items}")
print(f"all_test_duration = {round(all_test_duration / 3600, 2)}h")


