# sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh corebackup /ofs/corebackup 05b7b93388ef48cf932b72f4017c6e31 nmgpu
# sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speechssd /ofs/speechssd b46e06b5108e4fdd911a610d0faa5380 hbbpussd

source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
conda activate whisper

cd /nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune
# bash run_finetune_multimachine.sh > train_finetune_whisper_medium_data10w.log 2>&1
# bash run_finetune_multimachine.sh > /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune/medium_2w_data_fp32/finetune.log 2>&1
# bash run_finetune_multimachine.sh > /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_data_fp32_no_8k_2.0lr/finetune.log 2>&1
# bash run_finetune_multimachine.sh > /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_data_fp32_no_8k_2.0lr/finetune02.log 2>&1
# bash run_finetune_multimachine.sh > /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp16_3.0lr/finetune.log 2>&1
# bash run_finetune_multimachine.sh > /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune_2.0/medium_8w_without8k_fp32_5.0lr/finetune02.log 2>&1
# bash run_finetune_multimachine.sh
# bash run_finetune_multimachine_1_8.sh
bash run_finetune_multimachine_1_4.sh