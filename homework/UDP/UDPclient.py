import socket
udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    data=input("请输入消息")
    udp.sendto(data.encode("utf-8"),("127.0.0.1",8848))
    print(udp.recv(1024).decode("utf-8"))
udp.close()