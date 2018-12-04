
#原始数据如下：
v = {
'妖猫传':['黄轩','染谷将太'],
'无问西东':['章子怡','王力宏','祖峰'],
'超时空同居':['雷佳音','佟丽娅'],
}
name=input('输入一个明星：')
#刻印用while True循环
for movie in v:
    if name in v[movie]:
        print(name+'出演了电影'+movie)
        exit()
print('他啥都没演过')