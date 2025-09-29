#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import jsonlines
import string
import re
from tqdm import tqdm

def remove_punctuation(input_string):
    """去除所有标点符号"""
    translation_table = str.maketrans("", "", string.punctuation + "，。、；：！？（）【】『』“”《》［］｛｝﹙﹚﹛﹜﹝﹞〔〕〈〉")
    no_punct = input_string.translate(translation_table)
    return no_punct

# 需要转换的文件列表
data_list_filenames = ["data.list", "data_test.list", "data_train.list"]

for data_list_filename in data_list_filenames:
    
    total_items = 0
    total_correct_items = 0
    total_error_items = 0
    total_correct_duration = 0
    
    # 将 data.list 文件转换为 new_data.jsonl 文件
    whisper_json_filename = data_list_filename.replace("data", "new_data").replace(".list", ".jsonl")
    
    with open(data_list_filename, "r", encoding='utf-8') as data_list_file:
        contents = data_list_file.readlines()
        total_items = len(contents)
        
        with jsonlines.open(whisper_json_filename, mode="w") as whisper_json_file:
            for content in tqdm(contents, desc=f"Processing {data_list_filename}", unit=" lines"):
                
                # 获取各种文件信息
                audio_path, text, duration = content.strip().split("\t")
                
                # 去除标点符号
                text = remove_punctuation(text)
                
                result_json = {"audio": {"path": audio_path}, "sentence": text, "duration": duration}
                whisper_json_file.write(result_json)

                total_correct_items += 1
                total_correct_duration += float(duration)

    print(f"file_name = {data_list_filename}")
    print(f"total_items = {total_items}")
    print(f"total_correct_items = {total_correct_items}")
    print(f"total_error_items = {total_error_items}")
    print(f"total_correct_duration = {round(total_correct_duration / 3600, 2)}h")
