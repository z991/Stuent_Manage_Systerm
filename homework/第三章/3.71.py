import time

timesdata=time.time()
timesdata=int(timesdata%26)
print(chr(ord("a")+timesdata))
print(timesdata)