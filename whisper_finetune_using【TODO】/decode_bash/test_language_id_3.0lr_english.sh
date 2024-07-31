#!/bin/bash

# 挂载相关数据
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speech-datasets /ofs/speech-datasets dc680445ad5745c4871a9aeeebd988a4 nmgpu
sudo bash /mnt/com/nfs/volume-225-14/cuichenrui/scriptmon/jianshu/ofs/release/current/script/ofs_mount.sh corebackup /ofs/corebackup 05b7b93388ef48cf932b72f4017c6e31 nmgpu
sudo bash /mnt/common/jianshu/liquidio/release/current/script/liquid_mount_s3.sh  k80-dataset AKDD00000000000SGIPX2FHPLPMALX  ASDDCqkYLLUApBQrKInMsKjUECKbIZulHzdLTtlQ / /nfs/s3_k80_dataset
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speechssd /ofs/speechssd b46e06b5108e4fdd911a610d0faa5380 hbbpussd

# 激活代码环境
source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
conda activate whisper

# 处理的数据集列表
datasets=(
    "03_mix_chinese_and_english/mix_chinese_and_english" \
    "04_pure_english/pure_english" \
)

# 使用的模型列表
models=(
    "310000"
)

for dataset in "${datasets[@]}"; do
    for model in "${models[@]}"; do
        
        # 初始化相关变量
        hyp_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2/decode_logs/${dataset}_whisper_medium_3.0lr_english_${model}_hyp.txt"
        lab_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2/decode_logs/${dataset}_whisper_medium_3.0lr_english_${model}_lab.txt"
        norm_hyp_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2/decode_logs/${dataset}_whisper_medium_3.0lr_english_${model}_hyp_norm.txt"
        norm_lab_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2/decode_logs/${dataset}_whisper_medium_3.0lr_english_${model}_lab_norm.txt"
        test_data="/nfs/volume-225-14/cuichenrui/dataset/${dataset}.jsonl"
        model_path="/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_3.0lr/model_medium/checkpoint-${model}"
        log_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2/decode_logs/${dataset}_whisper_medium_3.0lr_english_${model}.log"
        cer_path="/nfs/volume-225-14/cuichenrui/whisper/experiment_decode_2/decode_logs/${dataset}_whisper_medium_3.0lr_english_${model}_cer.txt"

        # 解码whisper
        cd /nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune
        python evaluation_nolora.py \
            --hyp_path=$hyp_path \
            --lab_path=$lab_path \
            --test_data=$test_data \
            --model_path=$model_path \
            --batch_size=16 \
            --num_workers=8 \
            --language=English \
            --remove_pun=True \
            --to_simple=True \
            --timestamps=False \
            --min_audio_len=0.5 \
            --max_audio_len=30 \
            --local_files_only=True \
            --task=transcribe \
            --metric=cer \
            > $log_path 2>&1
        
        # hpy和lab文件文本归一化
        cd /nfs/volume-225-14/cuichenrui/whisper/experiment_decode/tools

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
