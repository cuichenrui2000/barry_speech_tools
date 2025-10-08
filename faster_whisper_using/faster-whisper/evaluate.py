#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from faster_whisper import WhisperModel
import json
import datetime
import argparse

result_dict = {}

def load_speech_data(path):
    """读取数据集"""
    with open(path, "r") as f:
        contents = f.readlines()
    return contents

parser = argparse.ArgumentParser()
parser.add_argument('--hyp_path', type=str, help="解码结果存储路径")
parser.add_argument('--lab_path', type=str, help="解码答案存储路径")
parser.add_argument('--test_data', type=str, help="测试数据集")
parser.add_argument('--model_path', type=str, help="模型路径")
args = parser.parse_args()

path = args.test_data
model_path = args.model_path
hyp_path = args.hyp_path
lab_path = args.lab_path

model = WhisperModel(model_path, device="cuda", compute_type="float16")
speech_data = load_speech_data((path))

total_duration = 0
decode_duration = 0

with open(hyp_path, "w") as f1, open(lab_path, "w") as f2:
    for line in speech_data:
        audio_path = json.loads(line)["audio"]["path"]
        label_text = json.loads(line)['sentence']
        duration = json.loads(line)['duration']

        # 此处作为 rtf 起始时间点
        starttime = datetime.datetime.now()
        
        # 这里可以添加各种解码超参数，详见 debug_faster_whisper_hyper_parameters.md
        segments, info = model.transcribe(audio_path, beam_size=5)
        predict_text = ""
        for segment in segments:
            predict_text += segment.text
        
        # 此处作为 rtf 结束时间点
        endtime = datetime.datetime.now()
        
        total_duration += duration
        decode_duration += (endtime - starttime).total_seconds()
        
        # 更新字典中对应字符的计数，不简洁但直观
        language_result = info.language
        if language_result in result_dict:
            result_dict[language_result] += 1
        else:
            result_dict[language_result] = 1
        
        print("Detected language '%s' with probability %f" % (language_result, info.language_probability))
        print(f"PATH: {audio_path}")
        print(f"LAB: {label_text}")
        print(f"HYP: {predict_text}")
        f1.write(audio_path + "\t" + predict_text + '\n')
        f2.write(audio_path + "\t" + label_text + '\n')  

# 打印总输出次数
total_output = sum(result_dict.values())
print("Total output:", total_output)

# 打印各个语言预测结果的比例，可以进行语种识别的准确率
print("Character counts:")
for char, count in result_dict.items():
    print(char, ":", count, round((count/total_output*100), 2), "%")

# 打印 rtf 相关信息
print(f"TOTAL_DURATION: {round(total_duration, 0)}s")
print(f"DECODEING_TIME: {round(decode_duration, 0)}s")
print(f"RTF: {round(decode_duration / total_duration, 4)}")