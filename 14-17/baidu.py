import requests

b=requests.get('https://www.baidu.com')
 #requests默认unicode编码，encode程utf8
b.encoding='utf8'

baidu=open('./baidu.html','w',encoding="utf8")

baidu.write(b.text)

baidu.close()