import librosa
import numpy as np
import soundfile
import torch

import random
import tarfile
import torchaudio
import logging

class TarFileDataset():
    def __init__(self, data_list_path):
        """
        Args:
            data_list_path: 数据列表文件的路径
            tar_filename_list: tar 文件名的临时存放列表，会在内部进行 shuffle
            audio_sample_list: audio 的临时存放列表，会在内部进行 shuffle
            sample_rate: 目标采样率，whisper 只适配 16k 音频，其他采样率会被强制转换至 16k 采样率再训练
        """
        self.data_list_path = data_list_path
        self.tar_filename_list = []
        self.audio_sample_list = []
        self.sample_rate = 16000
    
    # 返回一条音频组
    def get_one_sample(self):
        # 如果 tar_filename_list 空了，则补充，进入下一个 epoch
        if not self.tar_filename_list and not self.audio_sample_list:
            # 获取数据列表
            with open(self.data_list_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            for line in lines:
                # 读取文件中所有 tar 文件
                if line.strip().endswith('.tar'):
                    self.tar_filename_list.append(line.strip())
        # 如果 audio_sample_list 空了，则补充
        if not self.audio_sample_list:
            # 随机 pop 出一个 tar 文件名
            index_to_pop = random.choice(range(len(self.tar_filename_list)))
            tar_filename = self.tar_filename_list.pop(index_to_pop)
            stream = open(tar_filename, 'rb')
            # stream = tarfile.open(fileobj=stream, mode="r|*")
            stream = tarfile.open(fileobj=stream, mode="r:*")
            prev_prefix = None
            example = {}
            # valid 变量表示该数据是否正常，不正常就不返回
            valid = True
            for tarinfo in stream:
                name = tarinfo.name
                pos = name.rfind('.')
                assert pos > 0
                prefix, postfix = name[:pos], name[pos + 1:]
                if prev_prefix is not None and prefix != prev_prefix:
                    example['language'] = "chinese"
                    if valid:
                        self.audio_sample_list.append([example['sample'], example['sample_rate'], example['transcript'], example['language']]) 
                    example = {}
                    valid = True
                with stream.extractfile(tarinfo) as file_obj:
                    try:
                        if postfix == 'txt':
                            example['transcript'] = file_obj.read().decode('utf8').strip()
                        elif postfix in ['flac', 'mp3', 'm4a', 'ogg', 'opus', 'wav', 'wma']:
                            
                            # sample, sample_rate = soundfile.read(file_obj, dtype='float32')
                            sample, sample_rate = torchaudio.load(file_obj)
                            sample = sample.squeeze(0)
                            sample = sample.numpy()

                            # 判断音频时长是否为 0.5s ～ 30s
                            duration = len(sample) / sample_rate
                            if duration <= 0.5 or duration >= 30:
                                valid = False
                            sample = sample.T
                            if self.sample_rate != sample_rate:
                                sample = librosa.resample(sample, orig_sr=sample_rate, target_sr=self.sample_rate)
                            example['sample'], example['sample_rate'] = sample, sample_rate
                        else:
                            other_files = file_obj.read()
                    except Exception as ex:
                        logging.warning(ex, exc_info=True)
                        valid = False
                        logging.warning('error to parse {}'.format(name))        
                prev_prefix = prefix
            if prev_prefix is not None:
                example['language'] = "chinese"
                duration = len(example['sample']) / example['sample_rate']
                if duration > 0.5 and duration < 30:
                    self.audio_sample_list.append([example['sample'], example['sample_rate'], example['transcript'], example['language']]) 
            stream.close()
            # if 'process' in sample:
            #     sample['process'].communicate()
        # 随机 pop 出一个 audio_sample 文件名
        index_to_pop = random.choice(range(len(self.audio_sample_list)))
        audio_sample = self.audio_sample_list.pop(index_to_pop)
        # return sample, sample_rate, transcript, language
        return audio_sample[0], audio_sample[1], audio_sample[2], audio_sample[3]
