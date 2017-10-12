import socket
mystr="1_lbt4_10#32899#002481627512#0#0#0:1289671407:你的baby:你的hello:288:猥琐哥"

udp=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect(("10.10.153.162",2425))
udp.send(mystr.encode("gbk"))