sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speechssd /ofs/speechssd b46e06b5108e4fdd911a610d0faa5380 hbbpussd

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nfs/volume-225-14/cuichenrui/anaconda3/envs/TensorRT-LLM/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nfs/volume-225-14/laizhihao_i/env/anaconda3/envs/blsp/lib/python3.8/site-packages/nvidia/cudnn/lib

source /nfs/volume-225-14/cuichenrui/anaconda3/bin/activate
conda activate TensorRT-LLM

cd /nfs/volume-225-14/cuichenrui/TensorRT-LLM/examples/whisper

# choose the engine you build [./whisper_large_v3, ./whisper_large_weight_only]
output_dir=./whisper_outputs
# decode a single audio file
# If the input file does not have a .wav extension, ffmpeg needs to be installed with the following command:
# apt-get update && apt-get install -y ffmpeg
python run.py \
    --name single_wav_test \
    --assets_dir /nfs/volume-225-14/cuichenrui/TensorRT-LLM/examples/whisper/TensorRT-medium \
    --engine_dir $output_dir \
    --input_file /ofs/speechssd/datasets/s3_common_dataset/GigaSpeech/audio/AUD0000001679_S0001425.wav
# decode a whole dataset
# python3 run.py --engine_dir $output_dir --dataset hf-internal-testing/librispeech_asr_dummy --enable_warmup --name librispeech_dummy_large_v3_plugin