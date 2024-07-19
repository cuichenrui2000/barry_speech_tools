##  wenet 语音框架的使用

* [Github 开源地址](https://github.com/wenet-e2e/wenet.git)

* [Github 技术文档](https://wenet-e2e.github.io/wenet)

wenet 是出门问问语音团队联合西工大语音实验室开源的一款面向工业落地应用的语音识别工具包，该工具用一套简洁的方案提供了语音识别从训练到部署的一条龙服务，其主要特点如下：

* 使用 conformer 网络结构和 CTC / attention loss 联合优化方法，具有业界一流的识别效果。

* 提供云上和端上直接部署的方案，最小化模型训练和产品落地之间的工程工作。

* 框架简洁，模型训练部分完全基于 pytorch 生态，不依赖于 kaldi 等安装复杂的工具。

* 详细的注释和文档，十分适合用于学习端到端语音识别的基础知识和实现细节。

就我个人来讲，wenet 框架是我接触语音识别领域学习的第一个框架。wenet 框架非常的轻量，代码也十分通俗易懂，安装部署简介易用，网上的中文教程也非常多，非常适合作为语音识别的初学者学习了解。其独特的 attention rescoring 机制兼顾了流式的速度和模型的性能，很多实际场景都是基于 wenet 框架进行部署使用的。

作为第一次接触 wenet 框架的同学们，强烈建议跟随 ```wenet/examples/aishell/s0/run.sh``` 或者 ```wenet/examples/librispeech/s0/run.sh``` 走一遍整个语音识别的数据拉取，模型训练，模型解码，模型部署（可选）的流程，这会让你迅速了解语音识别这一领域。相关学习文档可参照本仓库的 ```barry_speech_tools/语音入门资料汇总.md``` 进行学习了解。

本人现在对其的使用场景主要为：

* wenetspeech 数据集的拉取

* 识别结果的 WER 和 CER 的检测

对于 wenetspeech 数据集，其是目前开源的最大的中文语音数据集，包含了 10000 小时左右的标签数据。但是其数据集比较复杂，还包括一些批量解压切分之类的操作，可以参照 ```wenet/examples/wenetspeech/s0/run.sh``` 进行拉取处理。

对于识别结果的 WER 和 CER 的检测，我们首先进行文本正则化，从而减少不同书写习惯带来的识别结果的不对齐，如 ```2.5平方电线``` 和 ```二点五平方电线``` ，具体实现细节可以参照下面的博客：

* [WeNet 丨 WeTextProcessing](https://blog.csdn.net/weixin_48827824/article/details/127207360)

然后我们进行 WER 和 CER 的计算，这里复制了 ```wenet/tools/compute-wer.py``` 的计算文件，整体流程可以查看 ```wenet_using/norm_and_conpute_cer.sh``` 脚本，我们只需准备识别结果 ```hyp.txt``` 和标签文件 ```lab.txt``` 即可，脚本将依次生成正则化后的识别结果 ```norm_hyp.txt``` 和正则化后的标签文件 ```norm_lab.txt```，和最终的 CER 计算结果文件 ```cer.txt```。中文会按字分割，英文会按词分割，wenet 的 CER 计算输出的结果非常直观，因此一直作为我个人最常用的 CER 检测工具。程序需要的 ```hyp.txt``` 和 ```lab.txt``` 格式如下：

```
# 每行格式为：<唯一标识符> \t <文本>
# 其中 <唯一标识符> 通常为音频路径，或音频路径的一部分
# 文本间不用进行空格去除，脚本会自动执行该步骤，中英混也可以自动识别

/your_audio_file/1.wav  这 是 第一条 音频
/your_audio_file/2.wav  This is 第二条 音频
/your_audio_file/3.wav  这是 the third 音频

        ... ...              ... ...

/your_audio_file/10000.wav  这是 the last audio
```

```wenet_using/train_mutimachine``` 提供了 wenet 单机多卡和多机多卡的训练启动脚本和 debug torchrun 的 vscode 格式的 ```wenet_using/train_mutimachine/vscode/launch.json``` 文件，希望可以对初次接触 torchrun 的你有所帮助。

总的来说，wenet 框架简单轻量，上手难度不大。其中文社区发展迅速，是非常优秀的语音识别框架，希望可以给大家带来帮助！
