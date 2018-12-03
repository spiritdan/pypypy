import bs4, requests, time
from urllib.request import quote

top250 = []
for page in range(0, 275, 25):
    url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='
    req = requests.get(url)
    bsmovie = bs4.BeautifulSoup(req.text, 'html.parser')
    list = bsmovie.select('#content li')

    for i in range(0, len(list)):
        # print(list[0])
        top_num = list[i].select('em')[0].getText()
        movie_details = list[i].select('.hd a span')

        top250.append(movie_details[0].getText())

print(top250)


def get_link(movie):
    movie_gbk = movie.encode('gbk')
    url = 'http://s.ygdy8.com/plus/so.php?kwtype=0&searchtype=title&keyword=' + quote(movie_gbk)
    req = requests.get(url)
    bsmovie = bs4.BeautifulSoup(req.text, 'html.parser')
    link = bsmovie.select('.co_content8 b a')
    finallink = 'http://www.ygdy8.com' + link[0].get('href')
    # print(finallink)
    req = requests.get(finallink).content.decode('gbk')
    bsmovie2 = bs4.BeautifulSoup(req, 'html.parser')
    movie_link = bsmovie2.select('.co_content8 table tbody  a')
    link = ''
    for i in range(0, len(movie_link)):
        # 延迟三秒，方式封IP
        time.sleep(3)
        link = '链接' + str(i) + ":" + movie_link[i].get('href')

    return link


# 由于数据量比较大，为了不影响系统运行，只下载前三部，
# print(get_link('金刚狼'))
for i in range(0, 3):
    print(top250[i])
    try:
        link = get_link(top250[i])

        print(top250[i] + ' ' + link)
    except:
        link = '网站未收录该部电影'
        print(top250[i] + ' ' + link)