import json
from tqdm import tqdm

text_dict = set()

with open("train_all_new_checked_without_8k.jsonl", 'r') as f:
    lines = f.readlines()
    for line in tqdm(lines, desc="Processing", unit="lines"):
        data = json.loads(line)
        sentence = data['sentence']

        for i in sentence:
            text_dict.add(i)

result = list(text_dict)
result.sort()
for i in result:
    print(i)
