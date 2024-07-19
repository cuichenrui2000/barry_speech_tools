##  Qwen-Audio 语音框架的使用

* [Qwen-Audio 论文](https://arxiv.org/abs/2311.07919)

* [Github 开源地址](https://github.com/QwenLM/Qwen-Audio)

* [Hugging face 模型地址](https://huggingface.co/Qwen/Qwen-Audio)

Qwen-Audio 是阿里开源的基于 LLM 的多任务语音系统，其使用 whisper encoder + LLM 结构，在多种语音任务上达到了非常好的性能。

就我个人而言，其模型设计思路和开源代码逻辑都是十分值得学习的，在本仓库提供了以下两个样例：

* Qwen-Audio 语音识别

* Qwen-Audio 哭声检测

###  Qwen-Audio 语音识别

Qwen-Audio 最为知名的就是其语音识别的能力，我们只需先替换 ```decode_mutimachine/evaluate_asr.py``` 文件，再执行 ```decode_mutimachine/qwen_audio_evaluate_cry.sh``` 脚本即可，数据 jsonl 格式如下：

```
# 数据列表采用 jsonl 格式，每行是一个 dict 元素

{"audio": /your_audio_file/1.wav, "text": audio_transcribe_text}
{"audio": /your_audio_file/2.wav, "text": audio_transcribe_text}
{"audio": /your_audio_file/3.wav, "text": audio_transcribe_text}

        ... ...              ... ...

{"audio": /your_audio_file/10000.wav, "text": audio_transcribe_text}
```

在解码过程中，速度奇慢无比，使用 8*A100 感觉 rtf 也在 0.6 左右，可以进行拉取学习，别真批量解码。对于 Qwen-Audio 的 ASR 结果，感觉效果确实不错，但是存在一些“同义不同表示”现象，如“高兴”识别成“开心”（例子很极端，能理解就好）。可以看出模型是完全理解语义的，并进行了自己的重新表述，我猜测原因来自于较小的 audio encoder 和巨大的 LLM decoder 之间的大小不匹配。

###  Qwen-Audio 哭声检测

Qwen-Audio 最为知名的就是其语音识别的能力，我们只需先替换 ```decode_mutimachine/evaluate_aqa.py``` 文件，再执行 ```decode_mutimachine/qwen_audio_evaluate_aqa.sh``` 脚本即可，数据 jsonl 格式如下：

```
# 数据列表采用 jsonl 格式，每行是一个 dict 元素
# question: 针对音频的问题
# audio: 音频路径
# gt: 这里是放和标签相关的，我们用不到，这里可以放任何你想要的信息
# source: 这里不知道是放什么的，我在这里又放了一遍针对音频的问题，方便打印结果

{"question": your_question, "audio": /your_audio_file/1.wav, "gt": you_can_put_some_other_things_here, "source": your_question}
{"question": your_question, "audio": /your_audio_file/2.wav, "gt": you_can_put_some_other_things_here, "source": your_question}
{"question": your_question, "audio": /your_audio_file/3.wav, "gt": you_can_put_some_other_things_here, "source": your_question}

        ... ...              ... ...

{"question": your_question, "audio": /your_audio_file/10000.wav, "gt": you_can_put_some_other_things_here, "source": your_question}
```

这个音频任务本来是音频问答，在官方提供的测试集上性能很好。但是我们的哭声检测任务模型在训练时基本没见过，所以经常会吐很多无关的话语（问他 yes or no 也不会只回答这俩词），应该是 unseen task 的原因，感觉进行少量的微调就能解决这个任务了。因为就输出结果来看，Qwen-Audio 知道哭声是什么样的，后续的微调我没有执行，感兴趣的同学可以进行一下尝试。

别的语音任务我还没进行尝试，感觉 Qwen-Audio 除了速度慢，别的没什么缺点，框架也清晰文档也全面，性能也很不错，推荐大家学习一下。