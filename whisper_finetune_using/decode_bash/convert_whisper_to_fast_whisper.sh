#!/bin/bash
# 2023_02_05

# 激活虚拟环境
source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
conda activate blsp

# 执行模型转换脚本
ct2-transformers-converter \
    --model /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_3.0/medium_kespeech_1e-4-fp32/checkpoint-310000/checkpoint-25000 \
    --output_dir /nfs/volume-225-14/cuichenrui/whisper/faster_whisper_models/whisper_kespeech_1e-4-fp32/checkpoint-25000 \
    --copy_files tokenizer.json preprocessor_config.json \
    --quantization float16
