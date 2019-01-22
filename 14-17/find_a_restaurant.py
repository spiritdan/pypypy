import requests
import json
import random
from sys import exit
'''
设计一个程序，用户只需要输入自己所在位置（如：腾讯大厦），即可弹出附近的餐厅名，供用户进行选择。（1）借助饿了么网站写爬虫。（2）可以帮你随机选一家餐厅去吃。（3）输出餐厅的名称和评分数据。程序随机出一个餐馆后，用户可以拒绝吃这一家，程序会重新启动随机，直到用户满意为止。
'''
# keyword='腾讯大厦'
keyword = input('输入一个地址：')
url = 'https://www.ele.me/restapi/shopping/restaurants/search?extras%5B%5D=activity&keyword=' + keyword + '&latitude=22.540822&limit=100&longitude=113.934457&offset=0&terminal=web'
res = requests.get(url)

while True:
    rand = random.choice(json.loads(res.text)['restaurant_with_foods'])
    # print(rand)
    json_value = rand['restaurant']
    # print(json_value['name'])

    answer = input('这家怎么样？' + json_value['name'] + ' 评分：' + str(json_value['rating']) + '(y/n)\n')
    if answer == 'y':
        print('地址：' + json_value['address'] + '\n电话：' + json_value['phone'])
        exit()
    else:
        print('我们再选一家')
