from flask import Flask, render_template, request
import requests
from fake_headers import Headers
import re
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_video(video_url):
    # 截取 https://v.douyin.com/FrsMefr/ 
    url = re.findall(r'https://v.douyin.com/.*?/', video_url)[0]
    # 获取重定向后的地址
    headers = Headers(os='mac', headers=True).generate()
    req = requests.get(url, headers=headers, allow_redirects=True)
    # req.url: https://www.douyin.com/video/7072769079551069447?previous_page=web_code_link
    video_id = re.findall('video\/(\d+)?', req.url)[0]
    data = requests.get(f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={video_id}', headers=headers).text
    video_address = json.loads(data)['item_list'][0]['video']['play_addr']['url_list'][0] 
    # 去水印
    video_address = video_address.replace('playwm', 'play')
    return video_address 

@app.route('/download_video', methods=['POST'])
def gen_video():
    video_url = request.form.get('video_url')
    if video_url:
        video = get_video(video_url)
        return render_template('index.html', video=video)
    return render_template('index.html', msg='地址不能为空')

if __name__ == '__main__':
    app.run(debug=True)
