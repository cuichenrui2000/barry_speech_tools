##  faster-whisper 语音框架的使用

* [Github 开源地址](https://github.com/SYSTRAN/faster-whisper)

* [Hugging face 模型地址](https://huggingface.co/Systran)

faster-whisper 是基于 OpenAI 的 Whisper 模型的高效实现，它利用 CTranslate2，一个专为 Transformer 模型设计的快速推理引擎。这种实现不仅提高了语音识别的速度，还优化了内存使用效率。faster-whisper 的核心优势在于其能够在保持原有模型准确度的同时，大幅提升处理速度，这使得它在处理大规模语音数据时更加高效。

就我个人而言，是在学习使用 Whisper 框架中了解到 faster-whisper 的，其性能确实非常高效，相比于 openai-whisper 还实现了一些额外的功能。faster-whisper 的相关功能和解码超参数可以参照本仓库的 ```faster_whisper_using/faster_whisper_hyper_parameters.md``` 文件，里面是我 debug 这个框架的一些分析思考，过程中 vscode 使用的 ```launch.json``` 文件也附在了 ```faster_whisper_using/vscode/launch.json``` 。

目录 ```faster-whisper``` 是我于 2024_05_11 在上述开源仓库克隆的版本 0.10.1。该仓库还在不断更新，不过基本框架没有太大变动。文件夹中的 ```faster-whisper/convert.sh``` , ```faster-whisper/evaluate.sh``` 和 ```faster-whisper/evaluate.py``` 文件是我自己写的解码相关代码。```faster-whisper/wenet_utils``` 是解码后处理的一些文件，拷贝自 wenet 框架，详细介绍可以参见本仓库 ```wenet_using``` 文件夹。

解码使用的数据集格式如下：

```
# 数据列表采用 jsonl 格式，每行是一个 dict 元素
# dict 中 duration 键对应的值为 float 格式，其余值均为 str 格式
# dict 中 language 和 duration 对应的值其实是没有用上的，但是为了整个框架数据的统一性，还是放在了数据集中
# jsonl 文件处理脚本可以参考本仓库的 data_processing 文件夹
# 数据列表格式沿用的是 whisper-finetune 项目框架，可以参考本仓库的 whisper_finetune 文件夹

{"audio": {"path": /your_audio_file/1.wav}, "sentence": audio_transcribe_text, "language": "your_audio_language", "duration": your_audio_duration}
{"audio": {"path": /your_audio_file/2.wav}, "sentence": audio_transcribe_text, "language": "your_audio_language", "duration": your_audio_duration}
{"audio": {"path": /your_audio_file/3.wav}, "sentence": audio_transcribe_text, "language": "your_audio_language", "duration": your_audio_duration}

        ... ...              ... ...

{"audio": {"path": /your_audio_file/10000.wav}, "sentence": audio_transcribe_text, "language": "your_audio_language", "duration": your_audio_duration}
```

执行脚本：

先执行 checkpoint 转换脚本，将 hugging face 格式的 checkpoint 转换为 faster-whisper 使用的 checkpoint：

```
. faster-whisper/convert.sh
```

然后执行解码脚本，该脚本执行解码、文本正则化、计算字错误率过程，另需要单独安装 wenet 环境，相关细节可以参见本仓库 ```wenet_using``` 文件夹：

```
. faster-whisper/evaluate.sh
```

这个脚本可以实现批量数据集，批量 checkpoint 的解码测试。测试程序不仅生成识别结果，同时还生成了语种识别的准确率和 rtf。缺点是解码的 batch_size 只能为 1 （faster-whisper框架所限制），导致用一些高性能卡时显存和算力都跑不满，不过可以单卡同时提交多个解码进程，具体细节再次不作赘述。

别的细节就没什么了，这个框架主要就是提供一个接口来加速 Whisper 的解码速度，不过 faster-whisper 的 VAD 时间戳好像还挺准的，有人通过这个框架实现了自动剪辑并生成字幕，还是挺有意思的，感兴趣的同学可以去了解一下。