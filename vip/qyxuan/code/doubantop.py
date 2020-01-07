import requests
from bs4 import BeautifulSoup
import lxml
import xlwt


headers ={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

def request_doubantop(url):
    try:
        response = requests.get(url, headers=headers,timeout=30) #为了网站反爬
        # print('status:{}'.format(response.status_code))
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = book.add_sheet('豆瓣电影top250', cell_overwrite_ok=True)
sheet.write(0,0,'名称')
sheet.write(0,1,'图片')
sheet.write(0,2,'排名')
sheet.write(0,3,'评分')
sheet.write(0,4,'作者')
sheet.write(0,5,'简介')

n = 1


def save_to_excel(soup):
    # print(soup.prettify())
    list = soup.find(class_='grid_view').find_all('li') #class_ 为了区分 内置class，在其后面添加一个下划线
    # print(list)
    for item in list:
        item_name = item.find(class_='title').string
        item_img = item.find('a').find('img').get('src')
        item_index = item.find(class_='').string
        item_score = item.find(class_='rating_num').string
        item_author = item.find('p').text.strip() # intr 也是 'p'标签，也何能精准定位到author
        item_intr = item.find(class_='inq').string

        print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
        # print('爬取电影：' + item_author )
        global n
        sheet.write(n,0,item_name)
        sheet.write(n,1,item_img)
        sheet.write(n,2,item_index)
        sheet.write(n,3,item_score)
        sheet.write(n,4,item_author)
        sheet.write(n,5,item_intr)
        n = n + 1

def main(page):
    url = 'https://movie.douban.com/top250?start=' + str(page*25) + '&filter='
    html = request_doubantop(url)
    soup = BeautifulSoup(html, 'lxml')
    save_to_excel(soup)


if __name__ == '__main__':
    for i in range(0, 10):
        main(i)

    book.save(u'豆瓣电影top250.xlsx')
