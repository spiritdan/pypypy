import requests,json,time
count=1
for i in range(1,6):
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p='+str(i)+'&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    res = requests.get(url)
    jsonres = json.loads(res.text)
    music = jsonres['data']['song']['list']
    for x in music:
        print('{0:03d}歌名：'.format(count)+x['name'])
        print('所属专辑：'+x['album']['name'])
        print('播放时长：'+str(x['interval'])+'秒')
        print('播放链接：https://y.qq.com/n/yqq/song/'+x['mid']+'.html\n\n')
        count+=1
    time.sleep(5)