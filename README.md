# 深度学习语音工具包

## 前言

## 00_语音入门资料
```
# 本模块将介绍语音入门的一些资料信息，包括但不限于语音的产生和语音数据结构，语音的特征提取（加窗分帧提特征），常见语音特征的使用等。
# TODO
```

### 入门基础教程

* [labuladong 的算法笔记](https://labuladong.github.io/algo)

* [CTC Loss原理](https://zhuanlan.zhihu.com/p/108547594)

* [一文入门元学习（Meta-Learning）（附代码）](https://zhuanlan.zhihu.com/p/136975128)

### 跟踪前沿动态进展

* [SUPERB 官网](https://superbbenchmark.org)

* [低调奋进](https://yqli.tech)

* [ICASSP 2023 官网](https://ieeexplore.ieee.org/document/10096024)

* [INTERSPEECH 2023 官网](https://www.isca-archive.org/interspeech_2023/index.html)

* [ICASSP 2024 官网](https://ieeexplore.ieee.org/xpl/conhome/10445798/proceeding)

### 简单上手项目汇总

* [栩栩如生, 音色克隆, Bert-vits2 文字转语音打造鬼畜视频实践 (Python3.10)](https://mp.weixin.qq.com/s/iXbX5-AbzKNF2pf1sSQIEA)

* [喂饭级 SO-VITS-SVC 教程，轻松生成 AI 歌曲](https://zhuanlan.zhihu.com/p/630115251)

* [GPT-SoVITS 整合包部署及使用教程](https://www.bilibili.com/read/cv30898214)

## 01_环境配置相关
```
# 本模块将介绍各种环境配置中容易踩的坑，本仓库实验环境为VSCode (集成开发环境) ➕ Anaconda (Python虚拟环境管理工具)
# 本模块将介绍我作为小白从0入门语音深度学习领域踩过的一些坑。
# TODO
```
### 容易踩坑的部分教程

这里是我之前踩过的一些坑，下面是相关教程链接的汇总，希望可以让你少走一些弯路。

VsCode是一款由微软开发的免费开源的代码编辑器，支持多种编程语言，并提供丰富的功能和插件。VsCode的灵活性和可定制性使其成为许多开发者首选的开发工具。我个人认为VsCode十分容易上手，各种插件也很丰富，唯一的缺陷是会给集群带来很高的负担，具体表现为不断占用cpu资源扫描你打开的文件目录实时更新；在home目录安装集群版本的.vscode-server文件，各种插件也安装于此，带来一些存储负担。但是这并不妨碍VsCode作为代码初学者的一款优秀上手工具。

* [vscode & windows terminal 实现远程服务器免密登录](https://www.jianshu.com/p/e3d63fa3ef63)

* [为什么 Mac 更新 Ventura 13.0 后 git / ssh 无法正常使用？](https://www.cnblogs.com/xhyccc/p/16836587.html)

* [Windows 使用 ssh 命令指定 .pem 文件出现: Load key "key.pem": Permission denied 和 Permissions for 'key.pem' are too open 问题](https://tool.4xseo.com/a/24567.html)

* [VSCode 中使用 jupyter notebook](https://zhuanlan.zhihu.com/p/140899377)

* [VSCode 中对 Python Cell 的原生支持 -- Run python Cells in VSCode](https://www.jianshu.com/p/fa90e902c6ae)

* [在 vscode 中对比两个文件夹的代码](https://zhuanlan.zhihu.com/p/677637988)

* [vscode切换虚拟环境，pip、pip3绑定系统python的问题](https://blog.csdn.net/Sharpneo/article/details/130527402)

Zotero是一款优秀的论文管理软件，拥有非常多的可拓展插件功能。强烈建议在开始大量阅读论文之前用Zotero养成良好的文献管理习惯，早用早安心。

* [Zotero：科研小白的第一款文献管理软件](https://zhuanlan.zhihu.com/p/347493385)

* [我的 Zotero 实践汇总](https://zhuanlan.zhihu.com/p/108366072)

* [文献管理神器 —— Zotero 配置及实用插件扩展](https://blog.csdn.net/qq_40918859/article/details/124380201)

* [文献管理软件 Zotero 常用插件安装及配置使用](https://blog.csdn.net/qq_43309940/article/details/117126357)

Tmux 介绍

* [Tmux 使用教程](https://www.ruanyifeng.com/blog/2019/10/tmux.html)

* [Tmux 常用快捷键](https://www.cnblogs.com/eirrac-rain/p/17803549.html)

Linux 相关环境配置

* [nvcc, cuda driver, cudatoolkit, cudnn 关系和区别](https://www.cnblogs.com/marsggbo/p/11838823)

* [conda 更新后激活环境不显示用户名和工作目录](https://blog.csdn.net/m0_56484411/article/details/127515359)

* [Linux 修改命令提示符前面的路径显示](https://blog.csdn.net/LSG_Down/article/details/112058574)

* [无 root 安装 cuda](https://zhuanlan.zhihu.com/p/476313656)

### 其他好用的工具汇总

* [ZEROTIER 多平台远程连接工具](https://www.zerotier.com)

* [PDF 格式转换工具](https://www.ilovepdf.com/zh-cn)

* [Convertio 格式转换](https://convertio.co/zh/webm-mp4)

* [SMS 虚拟电话号码购买](https://sms-activate.org/cn)

* [Apache ECharts 开源可视化图表库](https://echarts.apache.org/zh/index.html)

* [Pyecharts 教程](https://www.heywhale.com/mw/project/5eb7958f366f4d002d783d4a)

* [微软 Visio 流程图工具](https://www.microsoft.com/zh-cn/microsoft-365/visio/flowchart-software)

* [代码生成图片](https://www.jyshare.com/front-end/7433)

* [AI 生成图片](https://www.midjourney.com/home)

* [AI 生成音乐](https://mubert.com/render)

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

* [Github技术文档](https://wenet-e2e.github.io/wenet)

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

* [Fairseq 指南和源码解析](https://zhuanlan.zhihu.com/p/558760615)

* [浅讲 fairseq 的 ddp-backend 机制——原理和实现](https://zhuanlan.zhihu.com/p/580852851)

这里推荐知乎三元大佬的几篇博客：

* [基于判别学习的语音预训练模型（0）---简单总结](https://zhuanlan.zhihu.com/p/463864969)

* [基于判别学习的语音预训练模型（1）---从声学特征到自监督语音特征](https://zhuanlan.zhihu.com/p/463866895)

* [基于判别学习的语音预训练模型（2-1）---CPC from DeepMind](https://zhuanlan.zhihu.com/p/463867673)

* [基于判别学习的语音预训练模型（3-1）---wav2vec from FAIR](https://zhuanlan.zhihu.com/p/463868007)

* [基于判别学习的语音预训练模型（3-2）---vq-wav2vec from FAIR](https://zhuanlan.zhihu.com/p/463868373)

* [基于判别学习的语音预训练模型（3-3）---Discrete BERT from FAIR](https://zhuanlan.zhihu.com/p/463868745)

* [基于判别学习的语音预训练模型（3-4）---wav2vec 2.0 from FAIR](https://zhuanlan.zhihu.com/p/463869002)

* [基于判别学习的语音预训练模型（3-5）---wav2vec-U from FAIR](https://zhuanlan.zhihu.com/p/463869365)

* [基于判别学习的语音预训练模型（3-6）---wav2vec 2.0 + ST from FAIR](https://zhuanlan.zhihu.com/p/465112281)

* [基于判别学习的语音预训练模型（3-7）---HuBERT from FAIR](https://zhuanlan.zhihu.com/p/569958749)

* [基于判别学习的语音预训练模型（3-8）---wav2vec-U 2.0 from Meta AI](https://zhuanlan.zhihu.com/p/570234555)

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
