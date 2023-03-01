#-*- coding:UTF-8 -*-

import glob,os
import itchat
import time
from itchat.content import TEXT,PICTURE


itchat.auto_login(hotReload=True)
itchat.run()
current_path = os.getcwd()

imgs = []

def searchImage(text):
    print('收到关键词： ',text)
    for name in glob.glob('C:\\Users\\10500957\\github\\fxxkpython\\vip\\kelvinweng\\Spider\\*'+ text +'*.*'):
        imgs.append(name)

@itchat.msg_register(['PICTURE','TEXT'])
def text_reply(msg):
    searchImage(msg.text)
    for img in imgs[:2]:
        msg.user.send_image(img)
        time.sleep(0.4)
        print('开始发送表情：',img)
    imgs.clear()
    

