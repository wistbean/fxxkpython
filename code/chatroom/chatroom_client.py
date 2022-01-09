from tkinter import *
import socket
from threading import Thread

def get_msg():
    # 获取消息传入到消息面板
    while True:
        try:
            recv_msg = s.recv(1024).decode('utf8')
            msg_text.insert(END, recv_msg + '\n')
            msg_text.see(END)
        except:
            break

def on_press_enter(event):
    print('回车被按了一下')
    msg = input_text.get('0.0', END)
    # 发送消息到群里
    s.send(bytes(msg, 'utf8'))
    input_text.delete('0.0', END)

root = Tk()
root.title('深夜陪聊群')

# 监听事件
root.bind('<Return>', on_press_enter)

# 创建一个消息面板
msg_frame = Frame(
    root,
    width=480,
    height=390
)

# 创建一个输入面板
input_frame = Frame(
    root,
    width=480,
    height=100
)

msg_frame.grid_propagate(0)
input_frame.grid_propagate(0)

msg_text = Text(msg_frame)
input_text = Text(input_frame)

# 布局一下
msg_frame.grid(
    row=0,
    padx=3,
    pady=6
)

input_frame.grid(
    row=1,
    padx=3,
    pady=6
)

msg_text.grid()
input_text.grid()

# 接入socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6666))

# 获取服务端传来的信息
receive_thread = Thread(target=get_msg)
receive_thread.start()


root.mainloop()
