import requests
import re
import json

def requst_dangdang(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
    pattern = re.compile('<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span>.*?class="price_r">&yen;(.*?)</span>.*?</li>', re.S)
    # .*? 代表任意字符，用来衔接不同关键词，为了精准性，可适当增加关键词
    #（.*?）加了（）的表示需要筛选的内容
    items = re.findall(pattern, html)

    for item in items:
        yield {
            'range':item[0],
            'image':item[1],
            'title':item[2],
            'recommend':item[3],
            'author':item[4],
            'times':item[5],
            'price':item[6]
        }

def write_item_to_file(item):
    print("start write==>"+str(item))
    with open('book2.txt','a+',encoding='UTF-8') as ff:
        ff.write(json.dumps(item,ensure_ascii=False)+'\n')
        ff.close()

def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    html = requst_dangdang(url)
    items = parse_result(html)
    for item in items:
        write_item_to_file(item)

if __name__ == '__main__':
    for i in range(1,26):
        main(i)
