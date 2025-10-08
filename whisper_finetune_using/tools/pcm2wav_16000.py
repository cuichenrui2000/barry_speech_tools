import wave
import numpy as np

# 定义PCM文件和WAV文件的路径
pcm_file = '/nfs/volume-225-14/cuichenrui/dataset/8k.lst'

pcm_list = []
with open(pcm_file) as f:
    for line in f:
        pcm_list.append(line.strip())

# 设置音频参数
num_channels = 1  # 单声道
sample_width = 2  # 16位（2字节）采样深度
frame_rate = 16000  # 采样率，例如16000 Hz

for pcmfile in pcm_list:
    # 读取PCM文件
    with open(pcmfile, 'rb') as pcmf:
        pcm_data = pcmf.read()
    
        # 将PCM数据转换为NumPy数组
        pcm_array = np.frombuffer(pcm_data, dtype=np.int16)
    
        # 创建WAV文件并设置音频参数
        with wave.open(pcmfile.strip() + '.wav', 'wb') as wavfile:
            wavfile.setnchannels(num_channels)
            wavfile.setsampwidth(sample_width)
            wavfile.setframerate(frame_rate)
    
            # 将NumPy数组转换为二进制数据并写入WAV文件
            wavfile.writeframes(pcm_array.tobytes())
    
    print(f'Converted {pcmfile} to {pcmfile.strip() + ".wav"}')

