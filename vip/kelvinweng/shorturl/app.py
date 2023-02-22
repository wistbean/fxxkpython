from flask import Flask,request,render_template,redirect
import pyshorteners as psn
import sqlite3
import base62

host = 'http://127.0.0.1:5000/'
app = Flask(__name__) #表示这个py是作为单独模块启用，Flask就知道去哪里找模板和静态文件


@app.route('/')#FLask类的路由方法
def index():
    return render_template('index.html')#从template中导入hml模板
    
@app.route('/gen_short_url',methods = ['POST'])
def gen_short_url():
    long_url = request.form.get('long_url')#获取表单数据
    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO url (longurl) VALUES ('{}')".format(long_url))
    conn.commit()
    last_id = cursor.lastrowid
    encode = base62.encode(last_id)
    short_url = host + encode
    return render_template('index.html',short_url = short_url)

@app.route('/<encode_url>')
def redirect_url(encode_url):
    id = base62.decode(encode_url)
    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT longurl FROM url WHERE id LIKE ?",str(id))
        conn.commit()
        url = cursor.fetchone()
        return redirect(location=url[0])
    except sqlite3.Error as e:
        print (str(e))


    
if __name__ == '__main__':
    app.run()
