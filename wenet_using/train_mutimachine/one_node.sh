#!/bin/bash

cd "your_wenet_path"

# 激活 wenet 虚拟环境
source your_anaconda_path
conda activate your_faster_whisper_env_name

nvidia-smi
export NCCL_IB_DISABLE=1

num_nodes=1
num_gpus=8
job_id="your_job_id"
HOST_NODE_ADDR="localhost:0"

nj=16

train_set="your_train_set"
train_config="your_train_config"
dir="your_output_dir"
mkdir -p $dir

checkpoint=

. tools/parse_options.sh || exit 1;

# You have to rm `INIT_FILE` manually when you resume or restart a
# multi-machine training.
INIT_FILE=$dir/ddp_init
if [ -f ${INIT_FILE} ]; then
  rm ${INIT_FILE}
fi

torchrun --nnodes=$num_nodes --nproc_per_node=$num_gpus \
         --rdzv_id=$job_id --rdzv_backend="c10d" --rdzv_endpoint=$HOST_NODE_ADDR \
          wenet/bin/train.py \
          --config $train_config \
          --data_type raw \
          --train_data data/train/$train_set/data.list \
          --cv_data data/dev/data.list \
          ${checkpoint:+--checkpoint $checkpoint} \
          --model_dir $dir \
          --num_workers 8 \
          --pin_memory \
          --use_amp
