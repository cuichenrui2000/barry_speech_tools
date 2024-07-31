import os
from tqdm import tqdm
import librosa
import soundfile as sf
import json
import jsonlines

# 文件路径
input_file_path = "/nfs/volume-225-14/cuichenrui/dataset/02_general/general.jsonl"
output_file_path = "/nfs/volume-225-14/cuichenrui/dataset/02_general/general_8k.jsonl"
output_directory = "/ofs/speechssd/datasets/opensource_data/ASR/AISHELL_MAGICDATA_8K"
audio_datas = []

# 创建输出目录（如果不存在的话）
os.makedirs(output_directory, exist_ok=True)

# 读取文件路径
with open(input_file_path, 'r') as f:
    lines = f.readlines()
    for line in tqdm(lines, desc="read_old_json", unit="lines"):
        data = json.loads(line)
        audio_path = data['audio']['path']
        sentence = data['sentence']
        duration = data['duration']
        audio_datas.append((audio_path, sentence, duration))
        
# 处理并写入新文件
with jsonlines.open(output_file_path, mode="w") as output_file:
    # 处理每一个音频文件
    for audio_data in tqdm(audio_datas, desc="write_new_json", unit="lines"):
        audio_path = audio_data[0].strip()  # 去除行尾的换行符

        # 读取原始音频
        data, sr = librosa.load(audio_path, sr=None)

        # 检查采样率是否是16kHz
        if sr != 16000:
            print(f"Skipping {audio_path}, not 16kHz sample rate.")
            continue

        # 降采样到8kHz
        downsampled_data = librosa.resample(data, orig_sr=sr, target_sr=8000)

        # 获取新文件路径
        middle_path = os.path.dirname(audio_path.split("openSLR/")[1])
        base_name = os.path.basename(audio_path)
        new_folder_path = os.path.join(output_directory, middle_path)
        # 创建输出目录（如果不存在的话）
        os.makedirs(new_folder_path, exist_ok=True)
        new_file_path = os.path.join(new_folder_path, base_name)

        # 保存新文件
        sf.write(new_file_path, downsampled_data, 8000)
        # 写入json文件
        result_json = {"audio": {"path": new_file_path}, "sentence": audio_data[1], "language": "chinese", "duration": audio_data[2]}
        output_file.write(result_json)