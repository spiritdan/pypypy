#导入需要使用到的模块
import urllib
import re
import requests
import datetime
import pandas as pd
import pymysql
import os

#爬虫抓取网页函数
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('gbk')
    return html

#抓取网页股票代码函数
def getStackCode(html):
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    return code

Url = 'http://quote.eastmoney.com/stocklist.html'#东方财富网股票数据连接地址
filepath = 'D:\\stock_his\\'#定义数据文件保存路径
#实施抓取
code = getStackCode(getHtml(Url))
#获取所有股票代码（以6开头的，应该是沪市数据）集合
CodeList = []
for item in code:
    if item[0]=='6':
        CodeList.append(item)
print(CodeList)

'''
url = 'http://quotes.money.163.com/service/chddata.html?code=0600019&end=20181221&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
req=requests.get(url)
stock_list=[];
list=req.content.decode('gbk').replace('\'','').split()
for i in list:
    stock_list.append(tuple(i.split(',')))
print(stock_list)
'''

stock_list=[];
for code in CodeList:
    print('正在获取股票%s数据'%code)
    url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+\
        '&end=20181221&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
    req=requests.get(url)
    list=req.content.decode('gbk').replace('\'','').split()
    for i in list[1:]:      #list[0]是标题
        stock_list.append(tuple(i.split(','))) #executemany必须以元祖的格式传
        #print(stock_list)

'''
##########################将股票数据存入数据库###########################

#数据库名称和密码
name = 'root'
password = '123456'  #替换为自己的账户名和密码
#建立本地数据库连接(需要先开启数据库服务)
db = pymysql.connect('localhost', name, password, charset='utf8')
cursor = db.cursor()
try:
    #不存在就创建数据库stockDataBase
    sqlSentence1 = "Create Database If Not Exists stockDataBase"
    cursor.execute(sqlSentence1)

    #选择使用当前数据库
    sqlSentence2 = "use stockDataBase;"
    cursor.execute(sqlSentence2)
    
    #表不存在就创建
    sqlSentence3 = "Create Table If Not Exists `stock`.`NewTable`((日期 date, 股票代码 VARCHAR(10),     名称 VARCHAR(10),\
                       收盘价 float,    最高价    float, 最低价 float, 开盘价 float, 前收盘 float, 涨跌额    float, \
                       涨跌幅 float, 换手率 float, 成交量 bigint, 成交金额 bigint, 总市值 bigint, 流通市值 bigint)"
    cursor.execute(sqlSentence3)
except Exception as e:
    print(e)

begin = datetime.datetime.now()
end = datetime.datetime.now()
print(end-begin)

#获取本地文件列表
fileList = os.listdir(filepath)
#依次对每个数据文件进行存储
for fileName in fileList:
    try:

   #创建数据表，如果数据表已经存在，会跳过继续执行下面的步骤print('创建数据表stock_%s'% fileName[0:6])
        sqlSentence3 = "Create Table If Not Exists `stock`.`NewTable`((日期 date, 股票代码 VARCHAR(10),     名称 VARCHAR(10),\
                       收盘价 float,    最高价    float, 最低价 float, 开盘价 float, 前收盘 float, 涨跌额    float, \
                       涨跌幅 float, 换手率 float, 成交量 bigint, 成交金额 bigint, 总市值 bigint, 流通市值 bigint)"
        cursor.execute(sqlSentence3)
    except Exception as e:
        print(e)

    #迭代读取表中每行数据，依次存储（整表存储还没尝试过）
    print('正在存储stock_%s'% fileName[0:6])
    length = len(data)
    for i in range(0, length):
        record = tuple(data.loc[i])
        #插入数据语句
        try:
            sqlSentence4 = "insert into stock_%s" % fileName[0:6] + "(日期, 股票代码, 名称, 收盘价, 最高价, 最低价, 开盘价, 前收盘, 涨跌额, 涨跌幅, 换手率, \
            成交量, 成交金额, 总市值, 流通市值) values ('%s',%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" % record
            #获取的表中数据很乱，包含缺失值、Nnone、none等，插入数据库需要处理成空值
            sqlSentence4 = sqlSentence4.replace('nan','null').replace('None','null').replace('none','null')
            cursor.execute(sqlSentence4)
        except:
            #如果以上插入过程出错，跳过这条数据记录，继续往下进行
            break

#关闭游标，提交，关闭数据库连接
cursor.close()
db.commit()
db.close()
'''