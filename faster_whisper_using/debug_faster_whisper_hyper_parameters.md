### faster-whisper 相比于 openai-whisper 改进如下：

* 增加可选的外部 Silero VAD 模型, 可以为模型带来更好的 VAD 性能

* 通过结合 Cross-attention 和 DTW 算法，可以实现字级别的时间戳

* 使用 Ctranslate2 库，实现了模型 encode, detect_language, decode 的加速，大大降低了推理消耗

### 下面是我的 debug 结果：

* 我使用的 faster-whisper 接口是这样的：

```
from faster_whisper import WhisperModel

# 获取模型
model = WhisperModel(<your_model_path>, device="cuda", compute_type="float16")

# 获取音频路径
audio_path = <your_audio_path>

# 调用转录函数，此处注意设置 “without_timestamps=True” 与训练时保持一致
segments, info = model.transcribe(audio_path, beam_size=5, without_timestamps=True)

# 获取相应转录文本
predict_text = ""
for segment in segments:
    predict_text += segment.text
```

* 程序内部的超参数是这样的：
    
```
# 针对于某个音频，其 prompt 格式如下：[(“SOT_PRE”, “initial_prompt”), “3prompt tokens”, (“no_timestamp”), (“prefix”, “timestamp_begin”)]

# faster-whisper 解码时的超参数
options = TranscriptionOptions(
	beam_size=beam_size,                        	# 默认值5；beam search 的 beam size 参数
	best_of=best_of,                            	# 默认值5；温度非 0 时可供候选的结果数目
	patience=patience,                          	# 默认值1；beam search 的 patience 参数
	length_penalty=length_penalty,              	# 默认值1；输出 token 的长度惩罚项，是次方级别的数，model.generate() 使用
	repetition_penalty=repetition_penalty,      	# 默认值1；model.generate() 使用
	no_repeat_ngram_size=no_repeat_ngram_size,  	# 默认值0；model.generate() 使用
	log_prob_threshold=log_prob_threshold,	    	# 默认值-1.0；推理平均得分的下限，如果结果的平均得分比这个小，则温度提升重新跑	
	no_speech_threshold=no_speech_threshold,	# 默认值0.6；静音上限，如果结果的静音得分比这个大，则判定为静音，直接跳过本 segment
	compression_ratio_threshold=compression_ratio_threshold,    	# 默认值2.4；gzip 压缩比的抑制上限，如果生成结果的压缩比比这个大，则温度提升重新跑
	condition_on_previous_text=condition_on_previous_text,      	# 默认值True；前面的推理信息是否辅助下一部分的推理
	prompt_reset_on_temperature=prompt_reset_on_temperature,    	# 默认值0.5；温度大于这个阈值则重置 prompt，仅 compression_ratio_threshold 时生效
	temperatures=(									# 默认值[0.0, 0.2, 0.4, 0.6, 0.8, 1.0]；解码温度，
        temperature if isinstance(temperature, (list, tuple)) else [temperature]    	# 从 0 开始，不符合要求一直升高，最后都没合格结果会选择
    ),                                                                              	# 平均得分最高的结果   
	initial_prompt=initial_prompt,			# 默认值None；提供前缀提示，解码时拼到句子前面
	prefix=prefix,                              	# 默认值None；这个也是前缀提示，只有第一次解码的时候使用
	suppress_blank=suppress_blank,              	# 默认值True；model.generate() 使用
	suppress_tokens=get_suppressed_tokens(tokenizer, suppress_tokens),      	# 默认值[-1]；model.generate() 使用
	without_timestamps=without_timestamps,      	# 默认值True；是否需要时间戳，被我改成了False
	max_initial_timestamp=max_initial_timestamp,	# 默认值1.0；最大的起始时间戳，经过转换格式后；model.generate() 使用
	word_timestamps=word_timestamps,            	# 默认值False；是否需要字级别的时间戳，里面是个 force alignment，采用 cross-attention 和 DTW 算法
	prepend_punctuations=prepend_punctuations,  	# 默认值'"\'“¿([{-'；和字级别时间戳有关，标点符号和下一个字合并
	append_punctuations=append_punctuations,    	# 默认值'"\'.。,，!！?？:：”)]}、'；和字级别时间戳有关，标点符号和上一个字合并
)

# 内部 whisper 模型 generate 时的超参数
result = self.model.generate(
                encoder_output,
                [prompt],
                length_penalty=options.length_penalty,
                repetition_penalty=options.repetition_penalty,
                no_repeat_ngram_size=options.no_repeat_ngram_size,
                max_length=self.max_length,
                return_scores=True,
                return_no_speech_prob=True,
                suppress_blank=options.suppress_blank,
                suppress_tokens=options.suppress_tokens,
                max_initial_timestamp_index=max_initial_timestamp_index,
                **kwargs,
            )[0]

# 其中 temperature = 0 时
kwargs = {
                "beam_size": options.beam_size,
                "patience": options.patience,
                }

# 而当 temperature > 0 时
kwargs = {
                "beam_size": 1,
                "num_hypotheses": options.best_of,
                "sampling_topk": 0,
                "sampling_temperature": temperature,
                }
```

* debug 长音频中间结果如下：

```
[50258, 50267, 50359]
WhisperGenerationResult(sequences=[['<|0.00|>', 'æ²', 'Ī', 'éĺ', '³']], sequences_ids=[[50364, 3308, 230, 10034, 111]], scores=[-1.032812476158142], no_speech_prob=0.0)

[50361, 50364, 3308, 230, 10034, 111, 50258, 50267, 50359]
WhisperGenerationResult(sequences=[['<|0.00|>', 'ä½ł', 'å¹²', 'æ´»', 'ä¸Ģ', 'å¤©', 'äºĨ', 'éĥ½']], sequences_ids=[[50364, 2166, 26111, 25956, 2257, 6135, 2289, 7182]], scores=[-0.88427734375], no_speech_prob=5.960464477539063e-08)

[50361, 50364, 3308, 230, 10034, 111, 50364, 2166, 26111, 25956, 2257, 6135, 2289, 7182, 50258, 50267, 50359]
WhisperGenerationResult(sequences=[['<|0.00|>'], ['<|0.00|>'], ['<|0.00|>'], ['<|0.00|>'], ['<|0.00|>']], sequences_ids=[[50364], [50364], [50364], [50364], [50364]], scores=[-1.99951171875, -1.99951171875, -1.99951171875, -1.99951171875, -1.99951171875], no_speech_prob=5.960464477539063e-08)

... ... 依次类推... ...
```
