#!/bin/bash
export NCCL_IB_DISABLE=1

num_gpus=$RESOURCE_NUM_GPU

master_addr=$DISTRIBUTED_MASTER_HOSTS
master_port=$DISTRIBUTED_PYTORCH_PORT

num_nodes=$DISTRIBUTED_NODE_COUNT
node_rank=$DISTRIBUTED_NODE_RANK

echo $num_gpus $master_addr $master_port $num_nodes $node_rank
# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 torchrun --nproc_per_node=8 finetune.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/checkpoint --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data_small/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data_small/test/test.json
# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 torchrun --nproc_per_node=8 finetune.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_small --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/checkpoint/2w_data --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json
# CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 torchrun --nproc_per_node=$num_gpus finetune.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/checkpoint/2w_data --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/checkpoint/2w_data --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --resume_from_checkpoint=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/checkpoint/2w_data/model_medium/checkpoint-35000
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune/checkpoint/2w_data --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/laizhihao_i/Whisper/checkpoint/medium_data10w --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data_whole/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json 
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune/medium_2w_data_fp32 --train_data=/nfs/volume-225-14/laizhihao_i/data/train_data/train.json --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --fp16=False
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=2 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_data_fp32 --train_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/train_all_new_checked.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --fp16=False
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=2 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_data_fp32_no_8k_2.0lr --train_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/train_all_new_checked_without_8k.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --fp16=False
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=2 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_data_fp32_no_8k_2.0lr --train_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/train_all_new_checked_without_8k.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --fp16=False --resume_from_checkpoint=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_data_fp32_no_8k_2.0lr/model_medium/checkpoint-40000
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_3.0lr --train_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/train_all_new_checked_without_8k.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --fp16=True
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/laizhihao_i/Whisper/pretrain_model/model_medium --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp32_5.0lr --train_data=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/train_all_new_checked_without_8k_regularization.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test.json --fp16=True --resume_from_checkpoint=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp32_5.0lr/model_medium/checkpoint-160000
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_3.0lr/model_medium/checkpoint-310000 --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_3.0/medium_kespeech_5e-5-fp32 --train_data=/nfs/volume-225-14/cuichenrui/data_preparation/kespeech/kespeech_train.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test1.json --learning_rate=5e-5 --fp16=False
# torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_3.0lr/model_medium/checkpoint-310000 --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_3.0/medium_kespeech_1e-4-fp32 --train_data=/nfs/volume-225-14/cuichenrui/data_preparation/kespeech/kespeech_train.jsonl --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test1.json --learning_rate=1e-4 --fp16=False
torchrun --nproc_per_node=$num_gpus --nnodes=$num_nodes --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port finetune_multimachine.py --base_model=/nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_3.0lr/model_medium/checkpoint-310000 --per_device_train_batch_size=8 --per_device_eval_batch_size=8 --gradient_accumulation_steps=4 --num_workers=8 --output_dir=/nfs/dataset-411-391/speech2024/whisper/test/whisper_train_xingcheng --train_data=/nfs/dataset-411-391/wenet/examples/multi_cn/s0/data/train/filter_blank_zxbjjl_sichuanhua_national2.data --test_data=/nfs/volume-225-14/laizhihao_i/data/train_data/test1.json --learning_rate=5e-5 --fp16=True
