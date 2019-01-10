import requests
'''
（1）分别使用requests.text和.content下载《三国演义》第一回
（https://static.pandateacher.com/sanguo.md）。
（2）复制教材中下载音乐的代码并执行，听听看是什么歌
（https://static.pandateacher.com/py_1.mp3）。
（3）使用.content下载一张图片（https://gratisography.com/thumbnails/gratisography-318-thumbnail.jpg）。
'''
sanguo=requests.get('https://static.pandateacher.com/sanguo.md')
m=requests.get('https://static.pandateacher.com/py_1.mp3')
p=requests.get('https://gratisography.com/thumbnails/gratisography-318-thumbnail.jpg')

sanguo_txt=open('./sanguo.txt','w',encoding="utf8")
sanguo_for_txt=open('./sanguo_for.txt','w',encoding="utf8")
sanguo_content=open('./sanguo.content','wb')

music=open('./py_1.mp3','wb')
pic=open('./gratisography-318-thumbnail.jpg','wb')

sanguo_txt.write(sanguo.text)

for i in sanguo.text:
    try:
        sanguo_for_txt.write(i)
    except:
        pass
    continue

sanguo_content.write(sanguo.content)
sanguo.close()

music.write(m.content)
music.close()
pic.write(p.content)
pic.close()
