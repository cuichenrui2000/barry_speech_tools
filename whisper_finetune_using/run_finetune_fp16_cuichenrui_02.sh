#!/bin/bash

nvidia-smi

export NCCL_IB_DISABLE=1

num_nodes=3
node_rank=1
num_gpus=8
job_id=whisperMediumLoraFinetune01
HOST_NODE_ADDR="10.191.156.77:12348"
master_addr=10.191.156.77
master_port=12348

torchrun --nnodes=$num_nodes \
        --nproc_per_node=$num_gpus \
        --node_rank=$node_rank \
        --rdzv_id=$job_id \
        --rdzv_backend="c10d" \
        --rdzv_endpoint=$HOST_NODE_ADDR \
        --master_addr=$master_addr \
        --master_port=$master_port finetune_multimachine.py \
        --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium \
        --per_device_train_batch_size=2 \
        --per_device_eval_batch_size=4 \
        --gradient_accumulation_steps=5 \
        --num_workers=8 \
        --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_speed_test/A6000_environmrnt/whisper_medium_full_finetune_fp16/rank1 \
        --train_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_speed_test/train2wh_head10w.json \
        --test_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_speed_test/test2wh_head5000.json \
        --fp16=True \
