#通过使用socketserve类，TCPServe和StreamRequestHandler，该脚本创建了一个时间戳TCP服务器



from socketserver import StreamRequestHandler as SRH  # 选择 TCP的处理器类
from socketserver import TCPServer as TCP
from time import ctime

HOST = ''
PORT = 8888
BUFSIZE = 1024
ADDR = (HOST, PORT)

'''处理器类部分'''


class myTcp(SRH):  # 第二步：自定义处理器类的功能(这也是一个请求--request)
    def handle(self):
        print('client\'s address:', self.client_address),  # 打印连接上的客户端的 ip地址
        while True:
            data = self.request.recv(BUFSIZE)  # 从客户端接收信息
            if not data:
                break
            print(data.decode('utf-8'))
            reply = '[%s] %s' % (ctime(), data.decode('utf-8'))
            self.request.sendall(reply.encode('utf-8'))  # 向客户端发送信息


if __name__ == '__main__':
    '''服务器类部分'''
    tcpServ = TCP(ADDR, myTcp)  # 第一步：.选择一个服务器类，并创建其对象
    print("waiting for connecting...")
    tcpServ.serve_forever()  # 第三步：开启服务器
