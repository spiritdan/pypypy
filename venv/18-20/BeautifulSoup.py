import requests,bs4
#引用requests和bs4（BeautifulSoup4的缩写）,如果没有安装bs4，可以使用pip install beautifulsoup4下载。
from urllib.request import quote
#quote函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开。
movie = '创业时代'
gbkmovie=movie.encode('gbk')
#将汉字，用gbk格式编码，赋值给gbkmovie。
urlmovie = 'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword='+quote(gbkmovie)
#将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
res =requests.get(urlmovie)
#下载水形物语的搜索页面
bsmovie = bs4.BeautifulSoup(res.text,'html.parser')
#解析网页。
link = bsmovie.select('.co_content8 b a')
#查找目标。
finallink = 'http://www.ygdy8.com' + link[0].get('href')
#得到电影下载页的地址。
xiazai = requests.get(finallink).content.decode('gbk')
#使用requests模块，拿到电影下载页的源代码。使用content方法，拿到bytes数据，再进行decode，此时xiazai是字符串。
bsxiazai = bs4.BeautifulSoup(xiazai,'html.parser')
#解析网页。因为此时的xiazai已经是字符串，所以不需要加text。
download = bsxiazai.select('table tbody tr a')
#查找目标。
for x in download:
    print (x.get('href'))
print(len(download))