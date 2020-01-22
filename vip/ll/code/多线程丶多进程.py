import concurrent.futures
from bs4 import BeautifulSoup
import requests
header={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
movie = {}
def request(url):
    try:
        reponse=requests.get(url,headers=header)
        # rank=BeautifulSoup(reponse.content,'lxml').find('ol',class_='grid_view').find_all('em',class_="")
        movie_name=BeautifulSoup(reponse.content,'lxml').find('ol',class_='grid_view').find_all('img')
        for i in range(len(movie_name)):
             movie[movie_name[i]['alt']]=movie_name[i]['alt']
    except :
        print("error")
if __name__=="__main__":
    url=['https://movie.douban.com/top250?start='+str(i*25)+'&filter=' for i in range(0,10)]
    #
    # for i in url:
    #     request(i)
    #多线程爬取
    with concurrent.futures.ThreadPoolExecutor(max_workers=5)as executor:
        executor.map(request,url)
    #多进程爬取
    # with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        #executor.map(request, url)
    for count, value in enumerate(movie, 1):
        print(count, value)