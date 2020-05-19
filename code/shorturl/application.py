from flask import Flask, request, render_template, redirect
from bases import Bases
import pymysql

bases = Bases()
host = 'http://127.0.0.1:5000/'

try:
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 password='root',
                                 db='test',
                                 charset='utf8')
except pymysql.Error:
    raise 

cursor = connection.cursor()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/gen_short_url', methods=['POST'])
def gen_short_url():
    long_url = request.form.get('long-url')
    try:
        cursor.execute("INSERT INTO urls (url) VALUES ('{}')".format(long_url))
        connection.commit()
    except pymysql.Error:
        raise
    # 获取自增id
    last_id = cursor.lastrowid
    encode = bases.toBase62(last_id)
    short_url = host + encode
    return render_template('index.html', short_url=short_url)


@app.route('/<encode_url>')
def redirect_url(encode_url):
    id = bases.fromBase62(encode_url)
    try:
        cursor.execute("SELECT URL FROM urls WHERE id = " + str(id))
        connection.commit()
        url = cursor.fetchone()
        return redirect(location=url[0])
    except pymysql.Error as e:
        print(str(e))

if __name__ == '__main__':
    app.run(debug=True)
