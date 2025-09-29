# 2024_02_21
# 将whisper的jsonl格式转换为qwen的jsonl格式

input_filename = "map.jsonl"
output_filename = "qwen_map.jsonl"

import jsonlines

# 读取原始文件并转换格式
converted_data = []
with jsonlines.open(input_filename, "r") as input_file:
    for line in input_file:
        converted_data.append({
            "audio": line["audio"]["path"],
            "text": line["sentence"]
        })

# 将转换后的数据写入新文件
with jsonlines.open(output_filename, "w") as output_file:
    for data in converted_data:
        output_file.write(data)
