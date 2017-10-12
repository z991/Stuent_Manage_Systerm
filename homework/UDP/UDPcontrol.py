import socket
udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input("输入消息")
    udp.sendto(data.encode("utf-8"),("10.10.153.135",8848))
udp.close