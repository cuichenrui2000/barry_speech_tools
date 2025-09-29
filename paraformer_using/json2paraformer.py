import sys
import json

# 从命令行参数获取文件名
test_data_raw_file = sys.argv[1]
test_data_file = sys.argv[2]
lab_path_file = sys.argv[3]

# 打开文件并处理数据
with open(test_data_raw_file, 'r', encoding='utf-8') as raw_file, \
     open(test_data_file, 'w', encoding='utf-8') as data_file, \
     open(lab_path_file, 'w', encoding='utf-8') as lab_file:

    for line in raw_file:
        # 解析 JSON 行
        data = json.loads(line)
        
        # 提取路径和句子
        audio_path = data['audio']['path']
        sentence = data['sentence']
        
        # 写入 test_data 文件
        data_file.write(f"{audio_path}\t{audio_path}\n")
        
        # 写入 lab_path 文件
        lab_file.write(f"{audio_path}\t{sentence}\n")
