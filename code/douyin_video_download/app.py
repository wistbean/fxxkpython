from flask import Flask, request, render_template, redirect, Response, send_file
import requests
from fake_headers import Headers
import re
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def get_video(video_url):
    headers = Headers(os="mac", headers=True).generate()
    req = requests.get(video_url, headers=headers, allow_redirects=True)
    # print(req.url) https://www.iesdouyin.com/share/video/6967539188438813983
    video_id = re.findall('video\/(\d+)\/', req.url)[0]
    data_json = requests.get(f'https://www.iesdouyin.com/web/api/'
                             f'v2/aweme/iteminfo/?item_ids={video_id}').content
    video_addr = json.loads(data_json)['item_list'][0]['video']['play_addr']['url_list'][0]
    video_addr = video_addr.replace('playwm', 'play') #去水印

    path = f'static/cache/{video_id}.mp4'
    r = requests.get(video_addr, headers=headers, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return path



@app.route('/download_video', methods=['POST'])
def gen_video():
    video_url = request.form.get('video-url')
    if video_url:
        video = get_video(video_url)
        return render_template('index.html', video=video)

    return render_template('index.html', message='地址不能为空')



if __name__ == '__main__':
    app.run(debug=True)