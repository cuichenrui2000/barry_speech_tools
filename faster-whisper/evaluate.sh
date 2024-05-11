#!/bin/bash

# 处理的数据集列表，代码会依次找每一项名字 .jsonl 文件
# 如 datasets=("test01"），则会匹配到 test01.jsonl 文件
datasets_path="your_datasets_path"
datasets=(
    "test01" \
)

# 使用的模型列表，便于测试 whisper 的微调结果
# 你只需要给出 checkpoint 的 step 数就可以了，如 models=("100000")
# 如果你只需要测试开源的模型，可以忽略这一变量
model_path="your_model_path"
models=(
    "100000" \
)

# 解码结果输出路径
output_path="your_output_path"

# 如果输出路径不存在，则创建文件夹
if [ ! -d "$output_path" ]; then
    mkdir -p "$output_path"

for dataset in "${datasets[@]}"; do
    for model in "${models[@]}"; do
        
        # 初始化相关变量
        hyp_path="${output_path}/${dataset}_fast_whisper_${model}_hyp.txt"
        lab_path="${output_path}/${dataset}_fast_whisper_${model}_lab.txt"
        norm_hyp_path="${output_path}/${dataset}_fast_whisper_${model}_hyp_norm.txt"
        norm_lab_path="${output_path}/${dataset}_fast_whisper_${model}_lab_norm.txt"
        test_data="${datasets_path}/${dataset}.jsonl"
        model_path="${model_path}/checkpoint-${model}"
        log_path="${output_path}/${dataset}_fast_whisper_${model}.log"
        cer_path="${output_path}/${dataset}_fast_whisper_${model}_cer.txt"

        # 激活 faster-whisper 虚拟环境
        source your_anaconda_path
        conda activate your_faster_whisper_env_name

        # 解码 whisper
        python evaluate.py \
            --hyp_path=$hyp_path \
            --lab_path=$lab_path \
            --test_data=$test_data \
            --model_path=$model_path \
            > $log_path 2>&1
        
        # 激活 wenet 虚拟环境
        source your_anaconda_path
        conda activate your_wenet_env_name

        # hpy 和 lab 文件文本正则化
        cd wenet_utils

        python data_postprocessing.py \
            --raw_file_path=$hyp_path \
            --norm_file_path=$norm_hyp_path

        python data_postprocessing.py \
            --raw_file_path=$lab_path \
            --norm_file_path=$norm_lab_path

        # 计算 cer
        python compute-wer.py \
            --char=1 \
            --v=1 \
            $norm_lab_path \
            $norm_hyp_path \
            > $cer_path 2>&1

    done
done
