#!/bin/bash
# 2024_02_24
# paraformer批量解码脚本

# 挂载相关数据
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speech-datasets /ofs/speech-datasets dc680445ad5745c4871a9aeeebd988a4 nmgpu
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh corebackup /ofs/corebackup 05b7b93388ef48cf932b72f4017c6e31 nmgpu
sudo bash /mnt/common/jianshu/liquidio/release/current/script/liquid_mount_s3.sh  k80-dataset AKDD00000000000SGIPX2FHPLPMALX  ASDDCqkYLLUApBQrKInMsKjUECKbIZulHzdLTtlQ / /nfs/s3_k80_dataset
sudo bash /mnt/common/jianshu/ofs/release/current/script/ofs_mount.sh speechssd /ofs/speechssd b46e06b5108e4fdd911a610d0faa5380 hbbpussd

# 处理的数据集列表
datasets=(
    "01_in_car/01_map/map" \
    "01_in_car/02_music/music" \
    "01_in_car/03_car_control/car_control" \
    "01_in_car/04_dynamic/dynamic" \
    "01_in_car/05_static/static"
)
# datasets=(
#     "01_in_car/01_map/map" \
#     "01_in_car/02_music/music" \
#     "01_in_car/03_car_control/car_control" \
#     "01_in_car/04_dynamic/dynamic" \
#     "01_in_car/05_static/static" \
#     "02_general/general" \
#     "03_mix_chinese_and_english/mix_chinese_and_english" \
#     "04_pure_english/pure_english" \
#     "06_dialect/01_cantonese/cantonese_moved_test20000" \
#     "06_dialect/02_shanghai/shanghai_moved_test20000" \
#     "06_dialect/03_sichuan/sichuan_test20000" \
#     "07_customer_service/customer_service" \
#     "08_search/search"
# )

for dataset in "${datasets[@]}"; do
        
    # 初始化相关变量
    hyp_path="/nfs/volume-225-14/cuichenrui/paraformer/experimen_decode/${dataset}_hyp.txt"
    lab_path="/nfs/volume-225-14/cuichenrui/paraformer/experimen_decode/${dataset}_lab.txt"
    norm_hyp_path="/nfs/volume-225-14/cuichenrui/paraformer/experimen_decode/${dataset}_hyp_norm.txt"
    norm_lab_path="/nfs/volume-225-14/cuichenrui/paraformer/experimen_decode/${dataset}_lab_norm.txt"
    test_data_raw="/nfs/volume-225-14/cuichenrui/dataset/${dataset}.jsonl"
    test_data="/nfs/volume-225-14/cuichenrui/dataset/${dataset}.scp"
    output_path=$(echo "${hyp_path}}" | sed 's/^\(.*\)\/.*$/\1/')
    log_path="/nfs/volume-225-14/cuichenrui/paraformer/experimen_decode/${dataset}.log"
    cer_path="/nfs/volume-225-14/cuichenrui/paraformer/experimen_decode/${dataset}_cer.txt"

    # 激活paraformer解码环境
    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/nfs/volume-225-14/yanyuchen_i/tools/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
    eval "$__conda_setup"
    else
    if [ -f "/nfs/volume-225-14/yanyuchen_i/tools/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/nfs/volume-225-14/yanyuchen_i/tools/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/nfs/volume-225-14/yanyuchen_i/tools/miniconda3/bin:$PATH"
    fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<
    conda activate /nfs/volume-225-14/yanyuchen_i/envs/modelscope

    # 生成scp文件和lab文件
    python /nfs/volume-225-14/cuichenrui/dataset/json2paraformer.py \
            ${test_data_raw} \
            ${test_data} \
            ${lab_path}

    # 解码paraformer
    python /nfs/volume-225-35/huangpeiyao/paraformer/FunASR-main/hpy/para_scp.py \
            ${test_data} \
            ${output_path}

    # 将paraformer结果后处理生成hyp文件
    output_text_file=${output_path}/para_output/1best_recog/text
    python /nfs/volume-225-14/cuichenrui/paraformer/change_result.py \
            ${output_text_file} \
            ${hyp_path}

    # 激活代码环境
    source /nfs/volume-225-14/laizhihao_i/env/anaconda3/bin/activate
    conda activate whisper

    # hpy和lab文件文本归一化
    cd /nfs/volume-225-14/cuichenrui/whisper/experiment_decode/tools

    python data_postprocessing.py \
        --raw_file_path=$hyp_path \
        --norm_file_path=$norm_hyp_path

    python data_postprocessing.py \
        --raw_file_path=$lab_path \
        --norm_file_path=$norm_lab_path

    # 计算cer
    cd /nfs/volume-225-14/laizhihao_i/Wenet/wenet
    python tools/compute-wer.py \
        --char=1 \
        --v=1 \
        $norm_lab_path \
        $norm_hyp_path \
        > $cer_path 2>&1

done