import requests
import json
import webbrowser
from aip import AipSpeech
from arcade import load_sound,play_sound,stop_sound
import os

def respond(data):
    url = 'https://api.qingyunke.com/api.php?key=free&appid=0&msg=' + data
    result = requests.post(url)
    content = (result.content).decode('utf-8')
    str = json.loads(content)           #json可以字典化数据
    print ('Niubility:',str["content"])
    niubility_speek(str['content'])

def niubility_speek(data):
    APP_ID = '30817419'
    API_KEY= '1VCfu6wxK4v2eMbREm02DsXe'
    SECRET_KEY = 'ozoGHmabKzIyPFaO99V8h4kDWicNMC0U'

    client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
    result = client.synthesis(data,'zh',1,{
        'vol':5,
        'per':4,
        })
    if not isinstance(result,dict):
        with open('auido.mp3','wb') as f:
            f.write(result)
            f.close()
    
    
    
    sound = load_sound('auido.mp3')
    play_sound(sound)
    player = play_sound(sound)
    stop_sound(player)
    os.remove('auido.mp3')                  # 由于连续对话触发了权限问题，曲线救国，删除文件重新生成 
   

   
    
    
print ("超级好看的主人你好，我是Niubiliy，爱你哦，我有什么可以帮到你？")

while True:
    data = input ('你:')
    if data in "我想听歌":
        douban_url = "https://douban.fm/"
        webbrowser.get().open(douban_url)
    if data in "我想搜索":
        keywords = input("请输入您要搜索的内容:")
        sousuo_url = "https://www.baidu.com/s?wd=" + keywords
        webbrowser.get().open(sousuo_url)
    respond(data)

