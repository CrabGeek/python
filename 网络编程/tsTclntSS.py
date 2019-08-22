#基于socketServer类StreamRequest handler 对象通信
from socket import *

HOST = 'localhost'  # 我是本机操作，所以host写localhost，如果是连接外部的服务器，host就要等于服务器的ip地址
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

client = socket(AF_INET, SOCK_STREAM)
client.connect(ADDR)

while True:
    data = input('> ')
    if not data or data == 'exit':
        break

    client.send(data.encode('utf-8'))
    data = client.recv(BUFSIZE)

    if not data:
        break
    print(data.decode('utf-8'))

client.close()
