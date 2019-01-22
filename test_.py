import requests,bs4
from urllib.request import quote

urlmovie = 'http://market.finance.sina.com.cn/transHis.php?symbol=sz000002&date=2011-02-15&page=5'
#将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
res =requests.get(urlmovie)
bsmovie = bs4.BeautifulSoup(res.text,'html.parser')
print(bsmovie)
link = bsmovie.select('input[id="account"]')
print(link)
