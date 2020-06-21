"""
chat room 客户端
发送请求，获取结果
"""

from socket import *
from multiprocessing import Process

# 服务器地址
ADDR = ('127.0.0.1',8000)

# 进入聊天室
def login(sock):
    while True:
        name = input("Name:")
        msg = "L " + name # 根据协议，整理发送的消息格式 L name
        sock.sendto(msg.encode(),ADDR)
        result,add = sock.recvfrom(128)
        if result.decode() == "OK":
            print("进入聊天室")
            return
        else:
            print("该用户已存在")

def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    login(sock)
def fun():
    pass
def sec():
    pass
p = multiprocessing.Process(target=fun)
#启动进程，进程诞生，自动运行
p.start()
p.join()
if __name__ == '__main__':
    main()