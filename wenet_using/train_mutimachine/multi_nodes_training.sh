#!/bin/bash

cd "your_wenet_path"

# 激活 wenet 虚拟环境
source your_anaconda_path
conda activate your_faster_whisper_env_name

nvidia-smi
export NCCL_IB_DISABLE=1

num_gpus=$RESOURCE_NUM_GPU
master_addr=$DISTRIBUTED_MASTER_HOSTS
master_port=$DISTRIBUTED_PYTORCH_PORT

num_nodes=$DISTRIBUTED_NODE_COUNT
node_rank=$DISTRIBUTED_NODE_RANK
echo $num_gpus $master_addr $master_port $num_nodes $node_rank
job_id="your_job_id"
nj=16

train_set="your_train_set"
train_config="your_train_config"
dir="your_output_dir"
mkdir -p $dir
tensorboard_dir="your_tensorboard_dir"
checkpoint=

. tools/parse_options.sh || exit 1;

# You have to rm `INIT_FILE` manually when you resume or restart a
# multi-machine training.
INIT_FILE=$dir/ddp_init
if [ -f ${INIT_FILE} ]; then
  rm ${INIT_FILE}
fi

# cat /nfs/volume-225-13/zhangruixiong/wenet_space/wenet_xingcheng8k/examples/xingcheng8k/s0/data/train/exclude_sensitive_cantonese/16k_24000_tar.list /nfs/volume-225-13/zhangruixiong/training_data/sicheng_waihu.list /nfs/volume-225-13/zhangruixiong/wenet_space/wenet_xingcheng8k/examples/xingcheng8k/s0/data/train/exclude_sensitive/sensitive.list /nfs/volume-225-13/zhangruixiong/wenet_space/wenet_xingcheng8k/examples/xingcheng8k/s0/data/train/exclude_sensitive_cantonese/data_exclude_16ksearch_wenetspeech.list > /nfs/volume-225-13/zhangruixiong/wenet_space/wenet_xingcheng8k/examples/xingcheng8k/s0/data/train/exclude_sensitive_cantonese/16k_24000_sichangwaihu_sensitive_exclude_wenetspeech.list

torchrun --nnodes=$num_nodes --nproc_per_node=$num_gpus \
         --node_rank=$node_rank --master_addr=$master_addr --master_port=$master_port \
          wenet/bin/train.py \
          --config $train_config \
          --data_type mix \
          --train_data data/train/$train_set/data.list \
          --cv_data data/dev/data.list \
          --tensorboard_dir $tensorboard_dir \
          ${checkpoint:+--checkpoint $checkpoint} \
          --model_dir $dir \
          --num_workers 8 \
          --pin_memory \
          --use_amp
