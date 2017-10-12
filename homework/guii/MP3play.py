# -*- coding: UTF-8 -*-
import mp3play
import time

filename="D:\\1.mp3"
mp=mp3play.load(filename) #加载路径
mp.play()#播放
time.sleep(30)