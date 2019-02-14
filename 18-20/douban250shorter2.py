import bs4, requests
for page in range(0, 275, 25):
    req = requests.get('https://movie.douban.com/top250?start=' + str(page) + '&filter=')
    list = bs4.BeautifulSoup(req.text, 'html.parser').select('#content li')
    for i in range(0, len(list)):
        print(list[i].select('em')[0].getText(),end=' ')
        movie_details = list[i].select('.hd a span')
        print(''.join([movie.getText() for movie in movie_details]),end=' ')
        print(list[i].select('.rating_num')[0].getText())
