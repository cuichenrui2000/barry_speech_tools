#!/bin/bash

# 激活 faster-whisper 虚拟环境
source your_anaconda_path
conda activate your_faster_whisper_env_name

# 执行模型转换脚本
ct2-transformers-converter \
    --model your_hugging_face_model_path \
    --output_dir your_output_model_path[the_folder_should_not_exist] \
    --copy_files tokenizer.json preprocessor_config.json \
    --quantization float16
