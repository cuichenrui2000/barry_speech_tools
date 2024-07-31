#!/bin/bash

# 挂载相关数据
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speech-datasets /ofs/speech-datasets dc680445ad5745c4871a9aeeebd988a4 nmgpu
sudo bash /mnt/com/nfs/volume-225-14/cuichenrui/scriptmon/jianshu/ofs/release/current/script/ofs_mount.sh corebackup /ofs/corebackup 05b7b93388ef48cf932b72f4017c6e31 nmgpu
sudo bash /mnt/common/jianshu/liquidio/release/current/script/liquid_mount_s3.sh  k80-dataset AKDD00000000000SGIPX2FHPLPMALX  ASDDCqkYLLUApBQrKInMsKjUECKbIZulHzdLTtlQ / /nfs/s3_k80_dataset
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speechssd /ofs/speechssd b46e06b5108e4fdd911a610d0faa5380 hbbpussd

# 处理的数据集列表
datasets=(
    "04_pure_english/pure_english" \
)

# 使用的模型列表
models=(
    "310000"
)

for dataset in "${datasets[@]}"; do
    for model in "${models[@]}"; do
        
        # 初始化相关变量
        hyp_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/decode_logs/${dataset}_fast_whisper_medium_3.0_1.0_no_timestamp${model}_hyp.txt"
        lab_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/decode_logs/${dataset}_fast_whisper_medium_3.0_1.0_no_timestamp${model}_lab.txt"
        norm_hyp_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/decode_logs/${dataset}_fast_whisper_medium_3.0_1.0_no_timestamp${model}_hyp_norm.txt"
        norm_lab_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/decode_logs/${dataset}_fast_whisper_medium_3.0_1.0_no_timestamp${model}_lab_norm.txt"
        test_data="/nfs/volume-225-14/cuichenrui/dataset/${dataset}.jsonl"
        model_path="/nfs/volume-225-14/cuichenrui/whisper/faster_whisper_models/whisper_medium_3.0/checkpoint-${model}"
        log_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/decode_logs/${dataset}_fast_whisper_medium_3.0_1.0_no_timestamp${model}.log"
        cer_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/decode_logs/${dataset}_fast_whisper_medium_3.0_1.0_no_timestamp${model}_cer.txt"

        # 激活代码环境
        source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
        conda activate blsp

        # 解码whisper
        cd /nfs/volume-225-14/laizhihao_i/Whisper/faster-whisper
        python evaluate_cuichenrui_no_timestamp_choice_language.py \
            --hyp_path=$hyp_path \
            --lab_path=$lab_path \
            --test_data=$test_data \
            --model_path=$model_path \
            --language_id="en" \
            > $log_path 2>&1
        
        # 激活代码环境
        source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
        conda activate whisper

        # hpy和lab文件文本归一化
        cd /nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2_final/tools

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
done
