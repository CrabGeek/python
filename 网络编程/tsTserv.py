#TCP 时间戳服务器端

from socket import *
from time import ctime

HOST = "127.0.0.1"
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen()

while True:
    print('waiting for connection...')
    tcpCLiSock, addr = tcpSerSock.accept()
    print('...connected from :', addr)

    while True:
        data = tcpCLiSock.recv(BUFSIZE)
        if not data:
            break

        reply = '[%s] %s' % (ctime(), data.decode('utf-8'))
        tcpCLiSock.send(reply.encode())

    tcpCLiSock.close()

tcpSerSock.close()
