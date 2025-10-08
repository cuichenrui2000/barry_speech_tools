import sys

# 从命令行参数获取文件名
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# 打开输入文件并处理数据
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()

# 处理每一行数据
modified_lines = []
for line in lines:
    # 用制表符替换第一个空格
    modified_line = line.replace(' ', '\t', 1)
    modified_lines.append(modified_line)

# 将修改后的内容写入新文件
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    output_file.writelines(modified_lines)
