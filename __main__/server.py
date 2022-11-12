import socket
import threading

IP='127.0.0.1'
IPV6=False
PORT=8712

def init():
    # 初始化
    global server,clients_pool

    server=socket.socket(socket.AF_INET6 if IPV6 else socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP,PORT))
    server.listen(5)
    


if __name__ == '__main__':
    init()