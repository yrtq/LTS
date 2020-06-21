"""
author: Levi
email : lvze@tedu.cn
time:2020-6-13
env: Python3.6
socket and Process exercise
"""

from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)

# 存储用户  {name:address..}
user = {}

# 处理登录请求
def do_login(sock,name,address):
    if name in user:
        sock.sendto(b"Fail",address)
        return
    else:
        sock.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室"%name
        for i in user:
            sock.sendto(msg.encode(),user[i])
        # 存储用户
        user[name] = address
        print(user)


# 程序启动函数
def main():
    sock = socket(AF_INET,SOCK_DGRAM) # UDP
    sock.bind(ADDR)

    # 循环接收用户请求
    while True:
        # 接收用户请求 (所有客户端的所有请求都向这里发送)
        data,addr = sock.recvfrom(1024)
        tmp = data.decode().split(" ")
        # 根据请求调用模块
        if tmp[0] == 'L':
            # tmp-->['L','name']
            do_login(sock,tmp[1],addr)
        elif tmp[0] == 'C':
            pass





if __name__ == '__main__':
    main()



