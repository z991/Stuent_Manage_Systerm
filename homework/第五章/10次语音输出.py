'''import win32com.client
speaker=win32com.client.Dispatch("SAPI.SPVOICE")
num=0
while num<10:
    num=num+1
    print(num)
    speaker.Speak("你好")
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SPVOICE")
for num in range(0,11):
    speaker.Speak("你好")
'''

import win32com.client
speaker=win32com.client.Dispatch("SAPI.SPVOICE")
num=0
while num<100000:
    num=num+1
    if num>10:
        break
    speaker.Speak("你好")