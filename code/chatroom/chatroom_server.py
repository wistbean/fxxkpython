import socket
from threading import Thread

client = {}
addresses = {}

ACCEPT_NUM = 10
HOST = '127.0.0.1'
PORT = 6666

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

def handle_client_in(conn, addr):
    nikename = conn.recv(1024).decode('utf8')
    client[conn] = nikename
    # 群发消息
    broadcast(bytes(f'系统：{nikename}来了！！！', 'utf8'))

    # 转发用户的消息
    while True:
        try:
            msg = conn.recv(1024)
            broadcast(msg, nikename+':')
        except:
            del client[conn]
            broadcast(bytes(f'系统：{nikename}离开了！', 'utf8'))

def broadcast(msg, nikename=''):
    for conn in client:
        conn.send(bytes(nikename, 'utf8') + msg)

if __name__ == '__main__':
    s.listen(ACCEPT_NUM)
    print('服务器已经开启，正在监听用户的请求')

    while True:
        conn, address = s.accept()
        print(f'{address} 已经建立连接')
        # 给当前的连接对象发送消息
        conn.send('欢迎来到深夜陪聊群，请输入你的昵称开始嗨！'.encode('utf8'))
        addresses[conn] = address
        Thread(target=handle_client_in, args=(conn, address)).start()
