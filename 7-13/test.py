import requests,bs4
from bs4 import BeautifulSoup
url='https://www.autohome.com.cn/news/'
res=requests.get(url)
bsres=bs4.BeautifulSoup(res.content.decode('gbk'),'html.parser')
news=bsres.select('.article li a h3')
newsttl=news[0].getText()
print(newsttl)