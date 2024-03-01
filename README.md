# 深度学习语音工具包

## 前言

## 00_语音入门资料
```
# 本模块将介绍语音入门的一些资料信息，包括但不限于语音的产生和语音数据结构，语音的特征提取（加窗分帧提特征），常见语音特征的使用等。
# TODO
```

## 01_环境配置相关
```
# 本模块将介绍各种环境配置中容易踩的坑，本仓库实验环境为VSCode (集成开发环境) ➕ Anaconda (Python虚拟环境管理工具)
# 本模块将介绍我作为小白从0入门语音深度学习领域踩过的一些坑。
# TODO
```

## 02_数据处理相关
```
# 本模块将介绍各种语音数据的处理方法，对一个原始数据集的拉取和切分的一些方法汇总。
# Doing！！！
```

## 03_常用前端方法
```
# 本模块将介绍一些简单的前端处理方法，主要为数据集加噪加混响的常见方法，和一些经典易用的前端模型。
# TODO
```

## 04_常用识别方法
```
# 本模块将介绍一些一些常用的语音识别框架和模型，包括WeNet, ESPnet, Fairseq, Whisper, FunASR。
# TODO
```
### 各框架项目地址
```
# WeNet, ESPnet, Fairseq, Whisper, FunASR项目地址

# WeNet
git clone https://github.com/wenet-e2e/wenet.git

# ESPnet
git clone https://github.com/espnet/espnet.git

# Fairseq
git clone https://github.com/facebookresearch/fairseq.git

# Whisper
git clone https://github.com/openai/whisper.git

# FunASR
git clone https://github.com/alibaba-damo-academy/FunASR.git
```

### 01_wenet

Wenet是出门问问语音团队联合西工大语音实验室开源的一款面向工业落地应用的语音识别工具包，该工具用一套简洁的方案提供了语音识别从训练到部署的一条龙服务。

* [Github开源地址](https://github.com/wenet-e2e/wenet.git)

* [Github技术文档](https://wenet-e2e.github.io/wenet/)

在此附上4篇官方写的论文，可以更好得理解Wenet框架及其代表算法：

* [WeNet: Production Oriented Streaming and Non-streaming End-to-End Speech Recognition Toolkit](https://arxiv.org/pdf/2102.01547.pdf)

* [WeNet 2.0: More Productive End-to-End Speech Recognition Toolkit](https://arxiv.org/pdf/2203.15455v1.pdf)

* [Unified Streaming and Non-streaming Two-pass End-to-end Model for Speech Recognition](https://arxiv.org/pdf/2012.05481.pdf)

* [U2++: Unified Two-pass Bidirectional End-to-end Model for Speech Recognition](https://arxiv.org/pdf/2106.05642.pdf)

对于我个人来说，Wenet框架是我入门语音识别领域接触的第一个框架。相比于其他框架，Wenet框架更加轻量简洁，如果你作为语音识别初学者，强烈建议你跟着Github仓库的```examples/aishell/s0/run.sh```或者```examples/librispeech/s0/run.sh```依次按照每一个stage走一遍，代码非常清晰整洁，没有什么冗余的功能，注释也是十分详细的。

Wenet框架面向流式语音识别有一些独特的算法：

* Attention rescoring算法，可以理解为使用CTC进行第一遍流式解码，该结果可作为流式结果实时返回。然后对多个候选结果再通过attention-based decoder做一遍teacher forcing rescoring，根据得分重新排序，可以得到更好的识别结果。

* Conformer的流式改进算法，在self-attention层，将序列分成多个chunk，每帧在chunk内部做attention。这种方案可以保证对右侧依赖的长度与网络层数无关。Wenet在此之上使用了一种新的动态chunk训练算法，可以使得模型的chunk大小动态可变，在运行时，根据当前场景延时要求和识别率要求手动调整chunk大小，无需重新训练模型。

这里推荐知乎杨超大佬的几篇博客：

* [Wenet - 面向工业落地的E2E语音识别工具](https://zhuanlan.zhihu.com/p/349586567)

* [Wenet网络设计与实现1-端到端识别基础](https://zhuanlan.zhihu.com/p/381093937)

* [Wenet网络设计与实现2-网络结构](https://zhuanlan.zhihu.com/p/381095506)

* [Wenet网络设计与实现3-Mask](https://zhuanlan.zhihu.com/p/381271607)

* [Wenet网络设计与实现4-Cache](https://zhuanlan.zhihu.com/p/396703996)

看完这几篇博客，你会对整个Wenet框架有一个更加直观的理解。

对于我个人来说，Wenet框架简单轻量易上手，但是对于一些比较新的算法支持较少。我现在主要使用三个模块：# TODO

* WER和CER

* tn.chinese.normalizer

* Wenetspeech数据处理

### 02_espnet
```
# TODO
```

### 03_fairseq
```
# TODO
```

### 04_whisper
```
# TODO
```

### 05_FunASR
```
# TODO
```

## 05_音色迁移方法
```
# 本模块为我较为感兴趣的领域，在我之后的科研中如果有喜欢的合适的模型会在此进行分享介绍。
# TODO
```

## 06_常用合成方法
```
# 本模块为我较为感兴趣的领域，在我之后的科研中如果有喜欢的合适的模型会在此进行分享介绍。
# TODO
```
