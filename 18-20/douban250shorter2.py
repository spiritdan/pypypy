import bs4, requests
for page in range(0, 250, 25):
    req = requests.get('https://movie.douban.com/top250?start=' + str(page) + '&filter=')
    print('正在爬取第{0}页'.format(int(page/25+1)))
    list = bs4.BeautifulSoup(req.text, 'html.parser').select('#content li')
    [print(f"排名：{list[i].select('em')[0].getText()}\n电影名称：{list[i].select('.hd a span')[0].text}\n豆瓣评分：{list[i].select('.rating_num')[0].getText()}\n") for i in range(0, len(list))]
