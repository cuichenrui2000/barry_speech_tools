##  语音数据处理方法

这里将介绍一些语音数据的处理方法，包括如何拉取一个新的数据集，和一些典型的语音数据集处理方法。

### 数据处理操作

相关文件已汇总至文件夹 ```data_processing/data_using```，具体文件细节如下：

* pcm2wav.py【批量进行 pcm 文件至 wav 文件的转换，可设置采样率】

### 新数据集拉取

相关文件已汇总至文件夹 ```data_processing/prepare_new_corpus```，具体文件细节如下：

* check_file_existence.py【检验所有音频文件是否存在】

* convert_data_list_to_wenet_json.py【转换 data.list 数据格式至 wenet 数据格式】

* convert_wenet_data_to_whisper.py【转换 wenet 数据格式至 whisper 数据格式】

* do_copy_files.sh【数据迁移，多进程执行数据迁移脚本】

* make_copy_sh.py【数据迁移，制作 copy.sh】

* make_mkdir_sh.py【数据迁移，制作 mkdir.sh】

* make_new_data_list.py【数据迁移，制作新的 data.list，里面巧妙计算了音频 duration】

* make_train_and_test_data_existed.py【区分并生成训练集和测试集(已有测试集)】

* make_train_and_test_data.py【区分并生成训练集和测试集(未有测试集)】

* travel_and_make_all_wavpath_txt.py【数据迁移，制作 wavpath.txt】

### wenet 数据的使用

相关文件已汇总至文件 ```data_processing/wenet_data_using```，具体文件细节如下：

* data_regularization.py【数据文本正则化】

* data_split.py【切分数据集并重新排序，将简单数据集放到前面，困难数据集放到后面】

* get_new_dict.py【获取训练文本字典】

### whisper 数据的使用

相关文件已汇总至文件 ```data_processing/whisper_data_using```，具体文件细节如下：

* data_make_aishell2.py【制作 AISHELL-2 数据集】

* data_make_kespeech.py【制作 Kespeech 数据集】

* data_wav_exist_checking.py【检验 jsonl 文件中音频路径是否均存在】


