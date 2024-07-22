#!/bin/bash

CUDA_VISIBLE_DEVICES=0,1,2,3 torchrun --nproc_per_node=4 finetune_debug.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_small --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/checkpoint/model_small --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data_add8k/all8k_filter.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data_add8k/all8k_filter.json

