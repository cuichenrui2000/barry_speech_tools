#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import jsonlines
from tqdm import tqdm
    
# 需要拆分的数据前缀
a_list = "prefix_data_path1"
b_list = "prefix_data_path2"
c_list = "prefix_data_path3"

e_list = "prefix_data_path5"

a_file_name = "/nfs/volume-225-14/cuichenrui/data_preparation/1.list"
b_file_name = "/nfs/volume-225-14/cuichenrui/data_preparation/2.list"
c_file_name = "/nfs/volume-225-14/cuichenrui/data_preparation/3.list"
d_file_name = "/nfs/volume-225-14/cuichenrui/data_preparation/4.list"
e_file_name = "/nfs/volume-225-14/cuichenrui/data_preparation/5.list"

# 文件路径
raw_file_path = "your_raw_file_path"

# 逐行读取文件
with open(raw_file_path, "r") as file, \
    jsonlines.open(a_file_name, "w") as a_file, \
    jsonlines.open(b_file_name, "w") as b_file, \
    jsonlines.open(c_file_name, "w") as c_file, \
    jsonlines.open(d_file_name, "w") as d_file, \
    jsonlines.open(e_file_name, "w") as e_file:
    lines = file.readlines()
    for line in tqdm(lines, desc="Processing Checking", unit="lines"):
        
        # 解析 json 数据
        data = json.loads(line.strip())
        key = data["key"]
        wav = data["wav"]
        text = data["txt"]
        
        result_json = {"key": key, "wav": wav, "txt": text}
        
        if a_list in wav:
            a_file.write(result_json)
        elif b_list in wav:
            b_file.write(result_json)
        elif c_list in wav:
            c_file.write(result_json)
        elif e_list in wav:
            e_file.write(result_json)
        else:
            d_file.write(result_json)
