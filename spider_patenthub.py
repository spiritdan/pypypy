import requests,bs4
from urllib.request import quote

urlmovie = 'https://www.patenthub.cn/s?ds=all&q=ap%3A%22%E9%A9%AC%E9%9E%8D%E5%B1%B1%E9%92%A2%E9%93%81%22&fc=%5B%7B%22type%22%3A%22countryCode%22%2C%22op%22%3A%22include%22%2C%22values%22%3A%5B%22CN%22%5D%7D%5D'
#将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
res =requests.get(urlmovie)
bsmovie = bs4.BeautifulSoup(res.text,'html.parser')
print(bsmovie)
link = bsmovie.select('input[id="account"]')
print(link)
