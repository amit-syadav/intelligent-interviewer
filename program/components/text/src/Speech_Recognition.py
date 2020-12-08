# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:17:34 2020

@author: keval
"""
import os
import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

local_path = os.getcwd()
parent_path = os.path.dirname(local_path)
filename = os.path.join( str(parent_path) ,"audio","audio_wav3.wav")
harvard = sr.AudioFile(filename)
with harvard as source:
    audio = r.record(source)
type(audio)
print(r.recognize_google(audio))
