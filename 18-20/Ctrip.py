import bs4, requests
from urllib.request import quote
'''
抓取携程网站上，关于深圳欢乐谷的前三页评论：http://you.ctrip.com/sight/Shenzhen26/13720.html
提示：评论数据藏身于XHR中，但是数据需要使用BeautifulSoup模块解析。
'''
url = 'http://you.ctrip.com/destinationsite/TTDSecond/SharedView/AsynCommentView'
headers = {'Host': 'you.ctrip.com',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'Referer': 'http://you.ctrip.com/sight/Shenzhen26/13720.html'}
all_comment = []
spliter = '====================================='
for i in range(1, 4):
    page = 1
    data = {'poiID': '79101', 'districtId': '26', 'districtEName': 'Shenzhen', 'pagenow': str(page), 'order': '3.0',
            'star': '0.0', 'tourist': '0.0', 'resourceId': '13720', 'resourcetype': '2'}
    # print(data)
    r = requests.post(url, data=data, headers=headers)
    bs = bs4.BeautifulSoup(r.text, 'html.parser')
    # print(r.text)
    comment = bs.select('.main_con span')
    for j in range(0, len(comment)):
        all_comment.append(spliter + '第' + str(i) + '页 第' + str(j + 1) + '条评论' + spliter + '\n' + comment[0].getText())

print('\n'.join(all_comment))
# finallink='http://www.ygdy8.com' + link[0].get('href')
# print(finallink)
# req=requests.get(finallink).content.decode('gbk')
# bsmovie2=bs4.BeautifulSoup(req,'html.parser')
# movie_link=bsmovie2.select('.co_content8 table tbody  a')

# for i in range(0,len(movie_link)):
#    print('链接'+ str(i)+":"+movie_link[i].get('href'))