#!/bin/bash

# 处理的数据集列表
# datasets=(
#     "dynamic" \
#     "mix_chinese_and_english"
# )
datasets=(
    "general"
)

# 激活代码环境
source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
conda activate whisper

for dataset in "${datasets[@]}"; do

        hyp_path="/nfs/volume-225-14/cuichenrui/qwen/experimen_decode/${dataset}_hyp.jsonl"
        lab_path="/nfs/volume-225-14/cuichenrui/qwen/experimen_decode/${dataset}_lab.jsonl"
        norm_hyp_path="/nfs/volume-225-14/cuichenrui/qwen/experimen_decode/${dataset}_hyp_norm.txt"
        norm_lab_path="/nfs/volume-225-14/cuichenrui/qwen/experimen_decode/${dataset}_lab_norm.txt"
        cer_path="/nfs/volume-225-14/cuichenrui/qwen/experimen_decode/${dataset}_cer.txt"

        # hpy和lab文件文本归一化
        cd /nfs/volume-225-14/cuichenrui/qwen/tools

        python data_postprocessing.py \
            --raw_file_path=$hyp_path \
            --norm_file_path=$norm_hyp_path

        python data_postprocessing.py \
            --raw_file_path=$lab_path \
            --norm_file_path=$norm_lab_path

        # 计算cer
        cd /nfs/volume-225-14/laizhihao_i/Wenet/wenet
        python tools/compute-wer.py \
            --char=1 \
            --v=1 \
            $norm_lab_path \
            $norm_hyp_path \
            > $cer_path 2>&1

done
