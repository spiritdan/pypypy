# 已经抓取词典数据，因此不需要再运行
# 也可以去掉注释,每次启动会有点慢，但是可以及时更新数据
import requests, json, time

'''
link = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/')
f=open('./catalogy.txt','w')
f.write(link.text)
js_link = json.loads(link.text)
f.close()

for i in js_link['data']:
    print(i[0])
    test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category='+i[0])
    f=open('./'+i[0]+'.txt','w')
    f.write(test.text)
'''
f = open('./catalogy.txt', 'r')
link = f.read()
js_link = json.loads(link)
f.close()

bianhao = int(input('''请输入你选择的词库编号，按Enter确认
1，GMAT  2，考研  3，高考  4，四级  5，六级
6，英专  7，托福  8，GRE  9，雅思  10，任意
>'''))
ciku = js_link['data'][bianhao - 1][0]
test = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/?category=' + ciku)
f2 = open('./' + ciku + '.txt', 'r')
link = f2.read()
words = json.loads(link)
f.close()
# print(words)


check_words = []
known_words = []
unknow_words = []
word_ranks = []
print('测试现在开始。如果你认识这个单词，请输入Y，否则直接敲Enter：\n')
n = 0
for i in words['data']:
    n = n + 1
    word_ranks.append(str(i['rank']))
    print("第" + str(n) + '个：' + i['content'])
    answer = input('认识请敲Y，不认识请回车：\n')
    if answer.upper() == 'Y':
        check_words.append(i['content'])
        known_words.append(i)
    else:
        unknow_words.append(i)
print('\n在上述' + str(len(words['data'])) + '个单词当中，有' + str(len(check_words)) + '个是你觉得自己认识的，它们是：')
print(check_words)

print('现在我们来检测一下，你有没有真正掌握它们：')
wrong_words = []
right_ranks = []
right_num = 0
for y in known_words:
    print('\n\n')
    print('A:' + y['definition_choices'][0]['definition'])
    print('B:' + y['definition_choices'][1]['definition'])
    print('C:' + y['definition_choices'][2]['definition'])
    print('D:' + y['definition_choices'][3]['definition'])
    choice = input('请选择单词\"' + y['content'] + '\"的正确翻译：')
    dic = {'A': y['definition_choices'][0]['rank'], 'B': y['definition_choices'][1]['rank'],
           'C': y['definition_choices'][2]['rank'], 'D': y['definition_choices'][3]['rank']}
    if dic[choice.upper()] == y['rank']:
        right_ranks.append(str(y['rank']))
        right_num += 1
    else:
        wrong_words.append(y)
print('现在，到了公布成绩的时刻:')
print('在' + str(len(words['data'])) + '个' + js_link['data'][bianhao - 1][1] + '词汇当中，你认识其中' + str(
    len(check_words)) + '个，实际掌握' + str(right_num) + '个，错误' + str(len(wrong_words)) + '个。')
print('\n\n\n\n\n===================================================================================')

url = 'https://www.shanbay.com/api/v1/vocabtest/vocabularies/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'authority': 'www.shanbay.com', 'path': "/api/v1/vocabtest/vocabularies/"}

str1 = ','.join(right_ranks)

str2 = ','.join(word_ranks)
payload = {'category': ciku, 'phase': '', 'right_ranks': str1, 'word_ranks': str2}
# print(payload)
res = requests.post(url, data=payload, headers=headers)
# print(res.text)
dividewords = json.loads(res.text)['data']
print('您的词汇量：' + str(dividewords['vocab']))
print(dividewords['comment'])
print('\n\n===================================================================================')

save = input('是否打印并保存你的错词集？填入Y或N： ')
if save.upper() == 'Y':
    f = open('错题集.txt', 'a+')
    print('你记错的单词有：')
    f.write('你记错的单词有：\n')
    m = 0
    for z in wrong_words:
        m = m + 1
        # print (z['content'])
        rank = z['rank']
        for w in z['definition_choices']:
            if w['rank'] == rank:
                word_CN = w['definition']
        time.sleep(0.3)
        print(z['content'] + ' ' + word_CN)
        f.write(str(m + 1) + '. ' + z['content'] + word_CN + '\n')
    print('你不认识的单词有：')
    f.write('你没记住的单词有：\n')
    s = 0
    for i in unknow_words:
        print(i['content'])
        time.sleep(0.3)
        f.write(str(s + 1) + '. ' + i['content'] + '\n')
    print('错词和没记住的词已保存至当前文件目录下，下次见！')

else:
    print('下次见！')
