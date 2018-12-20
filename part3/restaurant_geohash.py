import requests
import json
import random
from sys import exit
#选到喜欢的馆子为止
url = 'https://www.ele.me/restapi/v2/pois?city_id=8&extras%5B%5D=count&geohash=wtw3sjq6n6um&keyword=%E5%8D%97%E4%BA%AC%E8%B7%AF&type=nearby'
res = requests.get(url)
json_value = json.loads(res.text)
print(res.text)
name_list = []
for i in json_value:
    print(i)