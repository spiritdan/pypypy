#payload = {'key1': 'value1', 'key2': 'value2'}
#把待上传的数据封装进一个字典
#r = requests.post("http://httpbin.org/post", data=payload)
#post函数需要两个参数，一个是网址，一个就是我们刚才封装好的那个字典，赋值给data。

import requests
import json

url = 'http://ictclas.nlpir.org/nlpir/index/getAllContentNew.do'
url2 = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
content = input('输入一段文字：')
data = {'type': 'all', 'content': content}
res = requests.post(url, data=data, headers=headers)
dividewords = json.loads(res.text)['dividewords']
# print(dividewords)
dividewords = dividewords.split(' ')
# print(dividewords)
newwords = []
# 创建一个空列表，命名为newwords。
cixing = []
# 创建一个空列表，命名为cixing。
for i in dividewords:
    if i == dividewords[-1]:
        continue
    temp = i.split('/');
    newwords.append(temp[0])
    cixing.append(temp[1])

dict = {'n': '名词', 'nr': '人名', 'nr1': '汉语姓氏', 'nr2': '汉语名字', 'nrj': '日语人名', 'nrf': '音译人名', 'ns': '地名', 'nsf': '音译地名',
        'nt': '机构团体名', 'nz': '其它专名', 'nl': '名词性惯用语', 'ng': '名词性语素',
        't': '时间词', 'tg': '时间词性语素', 's': '处所词', 'f': '方位词',
        'v': '动词', 'vd': '副动词', 'vn': '名动词', 'vshi': '动词“是”', 'vyou': '动词“有”', 'vf': '趋向动词', 'vx': '形式动词',
        'vi': '不及物动词（内动词）', 'vl': '动词性惯用语', 'vg': '动词性语素',
        'a': '形容词', 'ad': '副形词', 'an': '名形词', 'ag': '形容词性语素', 'al': '形容词性惯用语', 'b': '区别词', '': '', 'bl': '区别词性惯用语',
        'z': '状态词',
        'r': '代词', 'rr': '人称代词', 'rz': '指示代词', 'rzt': '时间指示代词', 'rzs': '处所指示代词', 'rzv': '谓词性指示代词', 'ry': '疑问代词',
        'ryt': '时间疑问代词', 'rys': '处所疑问代词', 'ryv': '谓词性疑问代词', 'rg': '代词性语素',
        'm': '数词', 'mq': '数量词', 'q': '量词', 'd': '副词', 'p': '介词', 'pba': '介词“把”', 'pbei': '介词“被”', 'c': '连词',
        'cc': '并列连词',
        'u': '助词', 'uzhe': '着', 'ule': '了，喽', 'uguo': '过', 'ude1': '的', 'ude2': '地', 'ude3': '得', 'usuo': '所',
        'udeng': '等，等等，云云', 'uyy': '一样，一般，似的，般', 'udh': '的话', 'uls': '来讲，来说，而言，说来', 'uzhi': '之', 'ulian': '连',
        'e': '叹词', 'y': '语气词', 'o': '拟声词', 'h': '前缀', 'k': '后缀', 'x': '字符串', 'xe': 'Email字符串', 'xs': '微博会话分隔符',
        'xm': '表情符合', 'xu': '网址URL',
        'w': '标点符号', 'wkz': '左括号', 'wky': '右括号', 'wyz': '左引号', 'wj': '句号', 'ww': '问号', 'wt': '叹号', 'wd': '逗号',
        'wf': '分号', 'wn': '顿号', 'wm': '冒号', 'ws': '省略号', 'wp': '破折号', 'wb': '百分号千分号', 'wh': '单位符号'
        }
cixing_list = []
for i in range(len(cixing)):
    cixing_list.append(newwords[i] + '/' + dict[cixing[i]])
new_cixing = " ".join(cixing_list)
print(new_cixing)

content = input('输入一个词：')
data = {'type': 'all', 'content': content}
res2 = requests.post(url2, data=data, headers=headers)
w2v_list = json.loads(res2.text)['w2vlist']
# print(w2v_list)
w2v_new = []
for i in w2v_list:
    w2v_new.append("'" + i.split(',')[0] + "'" + '相似度：' + i.split(',')[1])
'\n'.join(w2v_new)
print('\n'.join(w2v_new))
