import bs4,requests
import json
from urllib.request import quote

url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'
req=requests.get(url).content.decode()
print(req)
print(type(req))
j=json.loads(req)
print(j['subjects'])
for i in j['subjects']:
    print(i['title'])
'''
bsmovie=bs4.BeautifulSoup(req.text,'html.parser')
link=bsmovie.select('.co_content8 b a')
finallink='http://www.ygdy8.com' + link[0].get('href')
print(finallink)
req=requests.get(finallink).content.decode('gbk')
bsmovie2=bs4.BeautifulSoup(req,'html.parser')
movie_link=bsmovie2.select('.co_content8 table tbody  a')

for i in range(0,len(movie_link)):
    print('链接'+ str(i)+":"+movie_link[i].get('href'))
'''