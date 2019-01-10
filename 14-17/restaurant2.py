import requests
import json
import random
from sys import exit
#选到喜欢的馆子为止
url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws100xktc3b8&latitude=22.540822&limit=24&longitude=113.934457&offset=0&terminal=web'
res = requests.get(url)
json_value = json.loads(res.text)
name_list = []
for i in json_value:
    i['address'] = '苏州市观前街太监弄旁边的小路进去左转'
    name_list.append(i['name'])
# print(name_list)
while True:
    n = random.choice(name_list)
    for i in json_value:
        if i['name'] == n:
            answer = input('这家怎么样？' + i['name'] + ' 评分：' + str(i['rating']) + 'y/n\n')
            if answer == 'y':
                print('地址：' + i['address'] + '\n电话：' + i['phone'])
                exit()
            else:
                print('我们再选一家')


