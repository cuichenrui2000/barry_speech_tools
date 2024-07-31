sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speech-datasets /ofs/speech-datasets dc680445ad5745c4871a9aeeebd988a4 nmgpu
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh corebackup /ofs/corebackup 05b7b93388ef48cf932b72f4017c6e31 nmgpu
sudo bash /mnt/common/jianshu/liquidio/release/current/script/liquid_mount_s3.sh  k80-dataset AKDD00000000000SGIPX2FHPLPMALX  ASDDCqkYLLUApBQrKInMsKjUECKbIZulHzdLTtlQ / /nfs/s3_k80_dataset
sudo bash /mnt/com/nfs/volume-225-14/cuichenrui/scriptmon/jianshu/ofs/release/current/script/ofs_mount.sh corebackup /ofs/corebackup 05b7b93388ef48cf932b72f4017c6e31 nmgpu
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speechssd /ofs/speechssd b46e06b5108e4fdd911a610d0faa5380 hbbpussd

# source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
source /nfs/volume-225-14/cuichenrui/anaconda3/bin/activate
conda activate /nfs/volume-225-14/cuichenrui/anaconda3/envs/whisperA6000

cd /nfs/volume-225-14/laizhihao_i/Whisper/Whisper-Finetune
bash run_finetune_2wh_lr_cuichenrui_03.sh > /nfs/volume-225-14/cuichenrui/whisper/whisper_medium_full_finetune/medium_2w_data_fp32_1e-5lr/rank2/finetune.log 2>&1
