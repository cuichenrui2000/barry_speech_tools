export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nfs/volume-225-14/cuichenrui/anaconda3/envs/TensorRT-LLM/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nfs/volume-225-14/laizhihao_i/env/anaconda3/envs/blsp/lib/python3.8/site-packages/nvidia/cudnn/lib

source /nfs/volume-225-14/cuichenrui/anaconda3/bin/activate
conda activate TensorRT-LLM

cd /nfs/volume-225-14/cuichenrui/TensorRT-LLM/examples/whisper
python build.py \
        --world_size 1 \
        --model_dir /nfs/volume-225-14/cuichenrui/TensorRT-LLM/examples/whisper/TensorRT-medium \
        --model_name medium \
        --quantize_dir quantize/1-gpu \
        --dtype float16 \
        --log_level info \
        --max_batch_size 8 \
        --max_input_len 14 \
        --max_output_len 100 \
        --max_beam_width 4 \
        --use_gpt_attention_plugin \
        --use_bert_attention_plugin \
        --use_gemm_plugin \
        --output_dir whisper_outputs \
        --enable_context_fmha