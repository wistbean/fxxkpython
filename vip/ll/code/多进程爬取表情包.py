import  requests
from bs4 import BeautifulSoup
import os
import time
import concurrent.futures
import random
class BQB():
    def __init__(self):
        self.imgs_name=''
        self.page='/home/ly/桌面/test1'
        self.page=os.getcwd()
        self.header={'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    def request(self,url):
        try:
            # time.sleep(5)
            response=requests.get(url,headers=self.header)
            return response
        except:
            pass
    def get_url(self,url):#获取套图网页地址
        response=self.request(url)
        html_url=BeautifulSoup(response.content,'lxml').find('div',class_='col-sm-9 center-wrap').find_all('a')
        for i in html_url:#遍历套图网页地址
           # print(i['href'])
           self.get_img(i['href'])
           time.sleep(5)
    def get_img(self,url):#获取图片地址
        try:
            reponse = self.request(url)
            self.imgs_name = BeautifulSoup(reponse.content, 'lxml').find('div', class_="pic-title").get_text()
            img_url=BeautifulSoup(reponse.content,'lxml').find('div',class_='pic-content').find_all('img')
            os.mkdir(self.imgs_name)
            print("1")
            os.chdir(self.imgs_name)
            for i in img_url:#遍历图片地址

                self.save_img(i['src'],i['alt']+i['src'][-4:])
            os.chdir('/home/ly/桌面/test1')
        except:
           pass
    def save_img(self,url,name):#保存图片
        response = self.request(url)
        with open(name,'wb') as f:
              f.write(response.content)
              f.close()
        print(url+name)
if __name__=="__main__":
    url_1 = ["https://www.doutula.com/article/list/?page=" + str(i) for i in range(1,640)]
    bqb=BQB()
    with concurrent.futures.ProcessPoolExecutor(max_workers=3)as executor:
        executor.map(bqb.get_url, url_1)