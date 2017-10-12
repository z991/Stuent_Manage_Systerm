import  socket  #网络通信 TCP，UDP
import time
udpsever=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpsever.bind(("127.0.0.1",8848)) #绑定这个端口，接收这个端口的消息
while True:
    data,addr=udpsever.recvfrom(1024) #1024 缓冲区
    print("来自",addr,"消息",data)
    senddata=(data.decode("utf-8")+str(time.time())).encode("utf-8")
    udpsever.sendto(senddata,addr) #发送数据到指定的地址
