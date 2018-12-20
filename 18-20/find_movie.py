
import bs4,requests
from urllib.request import quote
movie=input('输入电影名称：')
movie_gbk=movie.encode('gbk')
url='http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword='+quote(movie_gbk)
req=requests.get(url)
bsmovie=bs4.BeautifulSoup(req.text,'html.parser')
link=bsmovie.select('.co_content8 b a')
finallink='http://www.ygdy8.com' + link[0].get('href')
print(finallink)
req=requests.get(finallink).content.decode('gbk')
bsmovie2=bs4.BeautifulSoup(req,'html.parser')
movie_link=bsmovie2.select('.co_content8 table tbody  a')

for i in range(0,len(movie_link)):
    print('链接'+ str(i)+":"+movie_link[i].get('href'))