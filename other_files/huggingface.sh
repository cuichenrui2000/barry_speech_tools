pip install huggingface_hub -i https://mirrors.aliyun.com/pypi/simple/
export HF_ENDPOINT=https://hf-mirror.com
huggingface-cli download \
  --repo-type dataset \
  --resume-download \
  --local-dir ./AVQA-Dataset \
  --local-dir-use-symlinks False \
  Vynce/AVQA-Dataset