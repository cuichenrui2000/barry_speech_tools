#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from transformers import WhisperProcessor

texts = ["This is an English sentence test hello I'm very glad to meet you", 
         "THIS IS AN ENGLISH SENTENCE TEST HELLO I'M VERY GLAD TO MEET YOU", 
         "this is an english sentence test hello i'm very glad to meet you", 
         "这是一条中文语句测试你好见到你很高兴", 
         "这是 一条 中文 语 句 测试 你好 见 到 你 很 高兴", 
         "这是一条中文语句测试，你好，见到你很高兴。"]

model_path = "your_model_path"

processor = WhisperProcessor.from_pretrained(model_path,
                                             language="English",
                                             task="transcribe",
                                             no_timestamps=True,
                                             local_files_only=True)

forced_decoder_ids = processor.get_decoder_prompt_ids()

for text in texts:
    
    token_ids = processor.tokenizer(text)["input_ids"]
    outputs = processor.tokenizer.batch_decode(token_ids, skip_special_tokens=True)
    
    print(f"原始句子：\n{text}")
    print(f"分词结果：\n{token_ids}")
    print(f"直观结果：\n{outputs}")
    print("\n")
