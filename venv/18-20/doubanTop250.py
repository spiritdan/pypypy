import bs4, requests

top250 = []
for page in range(0, 275, 25):
    url = 'https://movie.douban.com/top250?start=' + str(page) + '&filter='
    req = requests.get(url)
    bsmovie = bs4.BeautifulSoup(req.text, 'html.parser')
    list = bsmovie.select('#content li')
    print(list)
    for i in range(0, len(list)):

        # print(list[0])
        top_num = list[i].select('em')[0].getText()
        movie_details = list[i].select('.hd a span')
        # print(movie_details)
        movie_rate = list[i].select('.rating_num')[0].getText()
        temp = []
        for movie in movie_details:
            # print(movie.getText())
            temp.append(movie.getText())
            moviename = ''.join(temp)
        top250.append(top_num + '.' + moviename + ' 评分：' + movie_rate)
print('\n'.join(top250))