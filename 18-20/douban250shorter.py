import bs4, requests
top250 = []
for page in range(0, 275, 25):
    req = requests.get('https://movie.douban.com/top250?start=' + str(page) + '&filter=')
    list = bs4.BeautifulSoup(req.text, 'html.parser').select('#content li')
    for i in range(0, len(list)):
        top_num = list[i].select('em')[0].getText()
        movie_details = list[i].select('.hd a span')
        movie_rate = list[i].select('.rating_num')[0].getText()
        moviename = ''.join([movie.getText() for movie in movie_details])
        top250.append(top_num + '.' + moviename + ' 评分：' + movie_rate)
print('\n'.join(top250))