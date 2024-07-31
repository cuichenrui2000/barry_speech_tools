#!/bin/bash
# 使用本脚本需要先安装 wenet 框架和文本正则化的库

# 激活 wenet 虚拟环境
source your_anaconda_path
conda activate your_wenet_env_name

hyp_path="your_hyp_path"
lab_path="your_lab_path"
norm_hyp_path="your_norm_hyp_path_will_be_generated"
norm_lab_path="your_norm_lab_path_will_be_generated"
cer_path="your_cer_path_will_be_generated"

# hpy 和 lab 文件文本正则化
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
