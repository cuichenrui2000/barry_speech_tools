#!/bin/bash
export NCCL_IB_DISABLE=1

num_nodes=1
num_gpus=8
job_id=xingcheng8k
HOST_NODE_ADDR="localhost:0"

torchrun --nnodes=$num_nodes --nproc_per_node=$num_gpus --rdzv_id=$job_id --rdzv_backend="c10d" --rdzv_endpoint=$HOST_NODE_ADDR finetune_multimachine.py --base_model=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_6_id/model_medium/checkpoint-310000 --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/dataset-411-391/speech2024/whisper/test/whisper_train_xingcheng --train_data=/nfs/dataset-411-391/wenet/examples/multi_cn/s0/data/train/filter_blank_zxbjjl_sichuanhua_national2.data --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test1.json --learning_rate=5e-5 --fp16=True --use_tar_file_datalist=True
# torchrun --nnodes=$num_nodes --nproc_per_node=$num_gpus --rdzv_id=$job_id --rdzv_backend="c10d" --rdzv_endpoint=$HOST_NODE_ADDR finetune_multimachine.py --base_model=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_6_id/model_medium/checkpoint-310000 --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/dataset-411-391/speech2024/whisper/test/whisper_train_xingcheng --train_data=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/dataset/test_tar.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test1.json --learning_rate=5e-5 --fp16=True --use_tar_file_datalist=True