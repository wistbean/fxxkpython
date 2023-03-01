from flask import Flask, render_template, request, redirect
import pymysql
from bases import base62


bases = Bases()
host = 'http://127.0.0.1:5000/'


try:
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='test',
                                 charset='utf8'
                                 )
except pymysql.Error:
    raise

cursor = connection.cursor()


app = Flask('__name__')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gen_short_url', methods=['POST'])
def gen_short_url():
    long_url = request.form.get('long_url')
    # 将长链接存入数据库
    try:
        cursor.execute('insert into urls (url) values ("{}")'.format(long_url))
        connection.commit()
    except pymysql.Error:
        raise
    # 获取id
    last_id = cursor.lastrowid
    # 将 id 转化为 62 进制
    encode = bases.toBase62(last_id)
    short_url = host + encode 
    return render_template('index.html', short_url=short_url)


@app.route('/<encode_id>')
def redirect_url(encode_id):
    id = bases.fromBase62(encode_id)
    try:
        cursor.execute('select url from urls where id = {}'.format(id))
        connection.commit()
        url = cursor.fetchone()
        return redirect(url[0])
    except pymysql.Error:
        raise

