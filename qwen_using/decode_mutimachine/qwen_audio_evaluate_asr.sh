#!/bin/bash

# 处理的数据集列表，代码会依次找每一项名字 .jsonl 文件
# 如 datasets=("test01"），则会匹配到 test01.jsonl 文件
datasets_path="your_datasets_path"
datasets=(
    "test01" \
)

# 激活 qwen_audio 虚拟环境
source your_anaconda_path
conda activate your_qwen_audio_env_name

cd /your_qwen_audio_path/eval_audio

for dataset in "${datasets[@]}"; do

    # 初始化相关变量
    hyp_path="${output_path}/${dataset}_qwen_audio_${model}_hyp.txt"
    lab_path="${output_path}/${dataset}_qwen_audio_${model}_lab.txt"
    model_path="your_qwen_audio_model_path"
    log_path="${output_path}/${dataset}_qwen_audio_${model}.log"

    # 替换本仓库的 evaluate_asr.py 至 /your_qwen_audio_path/eval_audio 下的 evaluate_asr.py
    python3 -m torch.distributed.launch \
            --use-env \
            --nproc_per_node ${NPROC_PER_NODE:-8} \
            --nnodes 1 evaluate_asr.py \
            --checkpoint ${model_path} \
            --dataset ${dataset} \
            --batch-size 4 \
            --num-workers 8 \
            --hyp_path ${hyp_path} \
            --lab_path ${lab_path} \
            > ${log_path} 2>&1

done
