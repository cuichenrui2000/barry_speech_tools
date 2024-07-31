import json

input_file = "data.list"
output_file = "data_out.list"

with open(input_file, "r", encoding="utf-8") as f_in, open(output_file, "w", encoding="utf-8") as f_out:
    for line in f_in:
        # 解析每一行 JSON 数据
        data = json.loads(line.strip())
        
        # 提取 "wav" 和 "txt" 字段的值
        wav_value = data.get("wav", "")
        txt_value = data.get("txt", "")
        
        # 写入新文件，用 \t 分隔
        f_out.write(f"{wav_value}\t{txt_value}\n")

