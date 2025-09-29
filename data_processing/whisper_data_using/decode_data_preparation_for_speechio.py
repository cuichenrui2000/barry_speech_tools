#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonlines
from tqdm import tqdm
import os

filename_list = ["SPEECHIO_ASR_ZH00000", 
                "SPEECHIO_ASR_ZH00001", 
                "SPEECHIO_ASR_ZH00002", 
                "SPEECHIO_ASR_ZH00003", 
                "SPEECHIO_ASR_ZH00004", 
                "SPEECHIO_ASR_ZH00005"]

for i, filename in enumerate(filename_list):
    
    total_items = 0
    total_correct_items = 0
    total_error_items = 0
    total_correct_duration = 0
    
    metadata_filename = f"/ofs/speechssd/datasets/opensource_data/ASR/{filename}/metadata.tsv"
    whisper_json_filename = f"/nfs/volume-225-14/cuichenrui/dataset/12_speechio/0{i+1}_speechio0{i}/speechio0{i}.jsonl"

    with open(metadata_filename, "r") as metadata_file:
        
        contents = metadata_file.readlines()
        total_items = len(contents)
        
        with jsonlines.open(whisper_json_filename, mode="w") as whisper_json_file:
            
            for j, content in enumerate(tqdm(contents, desc="Processing contents")):

                # 跳过 csv 文件第一行
                if j == 0:
                    continue

                _, audio_path, duration, text = content.strip().split("\t")
                
                audio_path = metadata_filename[:-12] + audio_path
                if os.path.exists(audio_path):
                    duration = float(duration)
                    result_json = {"audio": {"path": audio_path}, "sentence": text, "language": "chinese", "duration": duration}
                    whisper_json_file.write(result_json)

                    total_correct_items += 1
                    total_correct_duration += duration

                else:
                    print("error audio path :" + audio_pathio)
                    total_error_items += 1

    print(f"total_items = {total_items}")
    print(f"total_correct_items = {total_correct_items}")
    print(f"total_error_items = {total_error_items}")
    print(f"total_correct_duration = {round(total_correct_duration / 3600, 2)}h")