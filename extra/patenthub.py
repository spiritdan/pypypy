import bs4, requests
from urllib.request import quote

url = 'https://www.patenthub.cn/user/login.json'
headers = {'Host': 'www.patenthub.cn',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'Referer': 'https://www.patenthub.cn/user/login.html'}
data = {'redirect_to':'https://www.patenthub.cn/','sso':'', 'account': '123','password': 'abc'}
#记录session
Soj_session = requests.session()
res = Soj_session.post(url, data=data, headers=headers)

name="马鞍山钢铁".encode('utf8')
r=Soj_session.get('https://www.patenthub.cn/s?ds=all&dm=mix&s=score%21&q='+quote(name))

bs = bs4.BeautifulSoup(r.text, 'html.parser')
list=bs.select('.ui .mix-mode')
print(list[0].select('span[data-property=title]'))
