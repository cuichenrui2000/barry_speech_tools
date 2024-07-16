##  语音数据处理方法

这里将介绍一些语音数据的处理方法，包括：TODO

### 数据集拉取

相关文件已汇总至文件 ```data_processing/data_traversal```

对于提供 ```wav.scp``` 或者 ```wav.lst``` 和 ```text.lst``` 这种数据集来说，直接做一个路径替换和音频文本的匹配就可以了。在此不提供示例，仅讲解如果没有这类汇总文件的数据集该如何遍历拉取。

首先你已经将数据集文件下载解压好了，假设数据集内部语音数据分布如下：
```
/.../your_dataset/scene001/number001/0000001.wav
/.../your_dataset/scene001/number001/0000001.txt

                    ... ...

/.../your_dataset/scene001/number001/0099999.wav
/.../your_dataset/scene099/number099/0099999.txt
```
即数据集内部有很多子文件夹，我们需要遍历整个文件夹来获取我们所需要的信息。对应文本信息要么为同名 txt 文件，要么为文件名等其他位置。数据处理的关键就是遍历当前文件夹下所有文件进行处理。```data_processing/data_traversal/data_traversal.py``` 文件尽可能地考虑了各种需求，为每条音频计算了 audio_path, audio_name, sentence, language, duration（这块有一个加速计算小技巧，性能远超 librosa 或者 pytorch 读取音频算时长），并使用可拓展性最强的 json 文件格式进行存储，大家完全可以根据需要改变相应的结果输出格式。示例启动脚本为 ```data_processing/data_traversal/data_traversal.sh```

### 数据集切分

相关文件已汇总至文件 ```data_processing/data_segmentation```


### 数据集迁移

相关文件已汇总至文件 ```data_processing/data_migration```



### 语音数据工具

相关文件已汇总至文件 ```data_processing/data_tools```
