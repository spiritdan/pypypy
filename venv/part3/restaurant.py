import requests
import json
import random
url = 'https://www.ele.me/restapi/shopping/restaurants?extras%5B%5D=activities&geohash=ws100xktc3b8&latitude=22.540822&limit=24&longitude=113.934457&offset=0&terminal=web'
res=requests.get(url)
url2='https://www.ele.me/restapi/v2/pois?extras%5B%5D=count&geohash=&keyword=%E5%87%AF%E5%8D%97%E5%B9%BF%E5%9C%BA&limit=20&type=nearby'
res2=requests.get(url2)
print(res2.text)
json_value=json.loads(res.text)
name_list=[]
for i in json_value:
    i['address']='苏州市观前街太监弄旁边的小路进去左转'
    name_list.append(i['name'])
#print(name_list)
n=random.choice(name_list)

for i in json_value:
    if i['name']==n:
        print("今天就吃这家吧："+i['name']+' ' +i['address']+' '+i['phone'])
