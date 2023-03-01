#-*- coding:utf-8 -*-
import requests
import os
import bs4
import time
import re
from bs4 import BeautifulSoup

download_url = 'https://www.doutuwang.com/category/dashijian/page/2'

page_num = 25

file_name = "D:\\测试图库"

image_down_url_1 = 'https://www.doutuwang.com'

def CreateFolder(file):
    flag = 1
    while flag == 1:
        if not os.path.exists(file):
            os.mkdir(file)
            flag = 0
        else:
            print('该文件已存在，请重新输入')
            flag = 1
            time.sleep(1)

    path = os.path.abspath(file)
        #print (path)

def DownloadPicture(download_url,list,path):
    r = requests.get(url=download_url,timeout=20)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text,'html.parser')

   
    tag = soup.find_all('img')

    j = 0
    for i in range(list,list+3):
        if(j <len(tag) and tag[j].attrs['src']!=None):
            img_name = str(i)+".jpg"
            image_down_url_2 = tag[j].attrs['src']
            j = j +1
            image_down_url = image_down_url_1 + image_down_url_2
            print ('image_down_url: ',image_down_url)


            try:
                img_data = requests.get(image_down_url)
            except:
                continue

            img_path = path + img_name
            with open(img_path,'wb') as fp:
                fp.write(img_data.content)
            print (img_name,'******下载完成')


if __name__=='__main__':
    path = "D:\\"
    print ('创建文件夹成功:',path)

    for i in range(0,page_num):
        if i == 0:
            page_url = download_url
        else:
            page_url = download_url[:-5]+"_"+str(i)+".html"

        DownloadPicture(page_url,i*3,path)

    print ("全部下载完成")

