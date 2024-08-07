#!/usr/bin/env python3
# -*- coding: utf-8 -*-

LANGUAGES = {
    "en": "英语",
    "zh": "中文",
    "de": "德语",
    "es": "西班牙语",
    "ru": "俄语",
    "ko": "韩语",
    "fr": "法语",
    "ja": "日语",
    "pt": "葡萄牙语",
    "tr": "土耳其语",
    "pl": "波兰语",
    "ca": "加泰罗尼亚语",
    "nl": "荷兰语",
    "ar": "阿拉伯语",
    "sv": "瑞典语",
    "it": "意大利语",
    "id": "印度尼西亚语",
    "hi": "印地语",
    "fi": "芬兰语",
    "vi": "越南语",
    "he": "希伯来语",
    "uk": "乌克兰语",
    "el": "希腊语",
    "ms": "马来语",
    "cs": "捷克语",
    "ro": "罗马尼亚语",
    "da": "丹麦语",
    "hu": "匈牙利语",
    "ta": "泰米尔语",
    "no": "挪威语",
    "th": "泰语",
    "ur": "乌尔都语",
    "hr": "克罗地亚语",
    "bg": "保加利亚语",
    "lt": "立陶宛语",
    "la": "拉丁语",
    "mi": "毛利语",
    "ml": "马拉雅拉姆语",
    "cy": "威尔士语",
    "sk": "斯洛伐克语",
    "te": "泰卢固语",
    "fa": "波斯语",
    "lv": "拉脱维亚语",
    "bn": "孟加拉语",
    "sr": "塞尔维亚语",
    "az": "阿塞拜疆语",
    "sl": "斯洛文尼亚语",
    "kn": "卡纳达语",
    "et": "爱沙尼亚语",
    "mk": "马其顿语",
    "br": "布列塔尼语",
    "eu": "巴斯克语",
    "is": "冰岛语",
    "hy": "亚美尼亚语",
    "ne": "尼泊尔语",
    "mn": "蒙古语",
    "bs": "波斯尼亚语",
    "kk": "哈萨克语",
    "sq": "阿尔巴尼亚语",
    "sw": "斯瓦希里语",
    "gl": "加利西亚语",
    "mr": "马拉地语",
    "pa": "旁遮普语",
    "si": "僧伽罗语",
    "km": "高棉语",
    "sn": "绍纳语",
    "yo": "约鲁巴语",
    "so": "索马里语",
    "af": "南非荷兰语",
    "oc": "奥克语",
    "ka": "格鲁吉亚语",
    "be": "白俄罗斯语",
    "tg": "塔吉克语",
    "sd": "信德语",
    "gu": "古吉拉特语",
    "am": "阿姆哈拉语",
    "yi": "意第绪语",
    "lo": "老挝语",
    "uz": "乌兹别克语",
    "fo": "法罗语",
    "ht": "海地克里奥尔语",
    "ps": "普什图语",
    "tk": "土库曼语",
    "nn": "新挪威语",
    "mt": "马耳他语",
    "sa": "梵文",
    "lb": "卢森堡语",
    "my": "缅甸语",
    "bo": "藏语",
    "tl": "他加禄语",
    "mg": "马尔加什语",
    "as": "阿萨姆语",
    "tt": "塔塔尔语",
    "haw": "夏威夷语",
    "ln": "林加拉语",
    "ha": "豪萨语",
    "ba": "巴什基尔语",
    "jw": "爪哇语",
    "su": "巽他语",
    "yue": "粤语",
}


['英语', '中文', '德语', '西班牙语', '俄语', '韩语', '法语', '日语', '葡萄牙语', '土耳其语', '波兰语', '加泰罗尼亚语', '荷兰语', '阿拉伯语', '瑞典语', '意大利语', '印度尼西亚语', '印地语', '芬兰语', '越南语', '希伯来语', '乌克兰语', '希腊语', '马来语', '捷克语', '罗马尼亚语', '丹麦语', '匈牙利语', '泰米尔语', '挪威语', '泰语', '乌尔都语', '克罗地亚语', '保加利亚语', '立陶宛语', '拉丁语', '毛利语', '马拉雅拉姆语', '威尔士语', '斯洛伐克语', '泰卢固语', '波斯语', '拉脱维亚语', '孟加拉语', '塞尔维亚语', '阿塞拜疆语', '斯洛文尼亚语', '坎纳达语', '爱沙尼亚语', '马其顿语', '布列塔尼语', '巴斯克语', '冰岛语', '亚美尼亚语', '尼泊尔语', '蒙古语', '波斯尼亚语', '哈萨克语', '阿尔巴尼亚语', '斯瓦希里语', '加利西亚语', '马拉地语', '旁遮普语', '僧伽罗语', '高棉语', '绍纳语', '约鲁巴语', '索马里语', '南非荷兰语', '奥克语', '格鲁吉亚语', '白俄罗斯语', '塔吉克语', '信德语', '古吉拉特语', '阿姆哈拉语', '意第绪语', '老挝语', '乌兹别克语', '法罗语', '海地克里奥尔语', '普什图语', '土库曼语', '新挪威语', '马耳他语', '梵文', '卢森堡语', '缅甸语', '藏语', '塔加洛语', '马尔加什语', '阿萨姆语', '鞑靼语', '夏威夷语', '林加拉语', '豪萨语', '巴什基尔语', '爪哇语', '巽他语', '缅甸语', '瓦伦西亚语', '佛兰芒语', '海地语', '卢森堡语', '普什图语', '旁遮普语', '摩尔达维亚语', '摩尔多瓦语', '僧伽罗语', '西班牙语']

LANGUAGES = {
    "en": "english",
    "zh": "chinese",
    "de": "german",
    "es": "spanish",
    "ru": "russian",
    "ko": "korean",
    "fr": "french",
    "ja": "japanese",
    "pt": "portuguese",
    "tr": "turkish",
    "pl": "polish",
    "ca": "catalan",
    "nl": "dutch",
    "ar": "arabic",
    "sv": "swedish",
    "it": "italian",
    "id": "indonesian",
    "hi": "hindi",
    "fi": "finnish",
    "vi": "vietnamese",
    "he": "hebrew",
    "uk": "ukrainian",
    "el": "greek",
    "ms": "malay",
    "cs": "czech",
    "ro": "romanian",
    "da": "danish",
    "hu": "hungarian",
    "ta": "tamil",
    "no": "norwegian",
    "th": "thai",
    "ur": "urdu",
    "hr": "croatian",
    "bg": "bulgarian",
    "lt": "lithuanian",
    "la": "latin",
    "mi": "maori",
    "ml": "malayalam",
    "cy": "welsh",
    "sk": "slovak",
    "te": "telugu",
    "fa": "persian",
    "lv": "latvian",
    "bn": "bengali",
    "sr": "serbian",
    "az": "azerbaijani",
    "sl": "slovenian",
    "kn": "kannada",
    "et": "estonian",
    "mk": "macedonian",
    "br": "breton",
    "eu": "basque",
    "is": "icelandic",
    "hy": "armenian",
    "ne": "nepali",
    "mn": "mongolian",
    "bs": "bosnian",
    "kk": "kazakh",
    "sq": "albanian",
    "sw": "swahili",
    "gl": "galician",
    "mr": "marathi",
    "pa": "punjabi",
    "si": "sinhala",
    "km": "khmer",
    "sn": "shona",
    "yo": "yoruba",
    "so": "somali",
    "af": "afrikaans",
    "oc": "occitan",
    "ka": "georgian",
    "be": "belarusian",
    "tg": "tajik",
    "sd": "sindhi",
    "gu": "gujarati",
    "am": "amharic",
    "yi": "yiddish",
    "lo": "lao",
    "uz": "uzbek",
    "fo": "faroese",
    "ht": "haitian creole",
    "ps": "pashto",
    "tk": "turkmen",
    "nn": "nynorsk",
    "mt": "maltese",
    "sa": "sanskrit",
    "lb": "luxembourgish",
    "my": "myanmar",
    "bo": "tibetan",
    "tl": "tagalog",
    "mg": "malagasy",
    "as": "assamese",
    "tt": "tatar",
    "haw": "hawaiian",
    "ln": "lingala",
    "ha": "hausa",
    "ba": "bashkir",
    "jw": "javanese",
    "su": "sundanese",
    "yue": "cantonese",
}