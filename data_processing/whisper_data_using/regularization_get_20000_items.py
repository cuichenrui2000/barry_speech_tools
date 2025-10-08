import random
from tqdm import tqdm

# 生成20000个随机数并排序
random_numbers = [random.randint(0, 8000) for _ in range(20000)]
line_number = 0

# 逐行读取两个文件的内容，并将对应行写入到shuffle_10000.jsonl文件中
with open('train_all_new_checked_without_8k.jsonl', 'r') as file1, \
        open('train_all_new_checked_without_8k_regularization.jsonl', 'r') as file2, \
        open('shuffle_20000.jsonl', 'w') as shuffle_file:
    
    for number in tqdm(random_numbers, desc="Processing", unit=" lines"):
        
        line_number += number + 1
        shuffle_file.write("行号：" + str(line_number) + "\n")
        # 跳过file1前number-1行
        for _ in range(number):
            next(file1)
        # 读取file1的第number行并写入到shuffle_file
        shuffle_file.write(next(file1))
        
        # 跳过file2前number-1行
        for _ in range(number):
            next(file2)
        # 读取file2的第number行并写入到shuffle_file
        shuffle_file.write(next(file2))
