# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:57:17 2020

@author: Nikus
"""

import pyttsx3

# 初始化
engine = pyttsx3.init()

voices = engine.getProperty('voices')
# 語速控制
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', rate - 20)

# 音量控制
volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', volume - 0.25)

engine.say('hello world')
engine.say('你好，世界')
# 朗讀一次
engine.runAndWait()

engine.say('語音合成開始')
engine.say('我會說中文了，開森，開森')
engine.runAndWait()

engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

# 更換語種--zh_HK
engine.setProperty('voice', "com.apple.speech.synthesis.voice.sin-ji")
engine.setProperty('voice', "VoiceGenderMale")
engine.say('從方法宣告上來看，第一個引數指定的是語音驅動的名稱，這個在底層適合作業系統密切相關的。')

# 更換語種--zh_CN
engine.setProperty('voice', "com.apple.speech.synthesis.voice.ting-ting.premium")
engine.say('從方法宣告上來看，第一個引數指定的是語音驅動的名稱，這個在底層適合作業系統密切相關的。')

# 更換語種--zh_TW
engine.setProperty('voice', "com.apple.speech.synthesis.voice.mei-jia")
engine.say('從方法宣告上來看，第一個引數指定的是語音驅動的名稱，這個在底層適合作業系統密切相關的。')
engine.runAndWait()

for voice in voices:
    print(voice)
    engine.setProperty("voice", voice.id)
