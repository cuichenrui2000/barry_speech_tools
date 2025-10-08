# 2024_02_20
# 数据准备脚本，将data.list转化为whisper可读的json文件

data_list_filenames = ["data_out.list"]

whisper_json_filename = "shunfengche.jsonl"

import json
import jsonlines
import soundfile
import string
import tqdm

def remove_punctuation(input_string):
    """去除所有标点符号"""
    translation_table = str.maketrans("", "", string.punctuation + "，。、；：！？（）【】『』“”《》［］｛｝﹙﹚﹛﹜﹝﹞〔〕〈〉")
    no_punct = input_string.translate(translation_table)
    return no_punct

total_items = 0
total_correct_items = 0
total_error_items = 0
total_correct_duration = 0
progress = 0

for data_list_filename in data_list_filenames:
    print(f"处理文件: {data_list_filename}")
    with open(data_list_filename, "r", encoding='utf-8') as data_list_file:
        contents = data_list_file.readlines()

        total_items = len(contents)
        
        with jsonlines.open(whisper_json_filename, mode="a") as whisper_json_file:
            for content in contents:
                progress += 1
                if progress % 100 == 0:
                    print(f"{progress} / {total_items}")

                audio_path, text = content.strip().split("\t")
                try:
                    text = remove_punctuation(text)
                    sample, sr = soundfile.read(audio_path)
                    duration = round(sample.shape[-1] / float(sr), 2)
                    result_json = {"audio": {"path": audio_path}, "sentence": text, "duration": duration}
                    whisper_json_file.write(result_json)

                    total_correct_items += 1
                    total_correct_duration += duration

                except Exception as e:
                    print("error audio path :" + audio)
                    total_error_items += 1

print(f"total_items = {total_items}")
print(f"total_correct_items = {total_correct_items}")
print(f"total_error_items = {total_error_items}")
print(f"total_correct_duration = {round(total_correct_duration / 3600, 2)}h")