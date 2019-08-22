# UDP 服务器，它接收客户端发来的信息， 并加入时间戳后返回

from socket import *
from time import ctime

HOST = ''
PROT = 21567
BUFSIZE = 1024
ADDR = (HOST, PROT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print("...wait for message")
    data, addr = udpSerSock.recvfrom(BUFSIZE)

    reply = '[%s] %s' %(ctime(), data.decode('utf-8'))

    udpSerSock.sendto(reply.encode(), addr)
    print("...receive message from and return to: ", addr)

udpSerSock.close()







