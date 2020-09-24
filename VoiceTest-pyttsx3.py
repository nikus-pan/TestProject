# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:55:32 2020

@author: Nikus
"""

import pyttsx3

engine = pyttsx3.init()
engine.say('hello world')
engine.say('你好，世界')
engine.runAndWait()
