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

def table_exists(con,table_name,db_name):
    sql = "use "+db_name+";"
    con.execute(sql)
    sql="show tables;"
    con.execute(sql)
    tables = [con.fetchall()]
    table_list = re.findall('(\'.*?\')',str(tables))
    table_list = [re.sub("'",'',each) for each in table_list]
    if table_name in table_list:
        return True
    else:
        return False

def db_exists(con,db_name):
    sql = "show databases;"
    con.execute(sql)
    db = [con.fetchall()]
    db_list = re.findall('(\'.*?\')',str(db))
    db_list = [re.sub("'",'',each) for each in db_list]
    if db_name in db_list:
        return True
    else:
        return False

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

stock_list=[];
print("开始爬取数据")
begin = datetime.datetime.now()
#
for code in CodeList:
    print('正在获取股票%s数据'%code)
    url = 'http://quotes.money.163.com/service/chddata.html?code=0'+code+\
        '&end=20181221&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
    req=requests.get(url)
    list=req.content.decode('gbk').replace('\'','').split('\r\n')

    for i in list[1:]:      #略过list[0]标题
        if i !="":
            stock_list.append(tuple(i.split(','))) #executemany必须以元祖的格式传
#for j in stock_list:
#    print(j)
end = datetime.datetime.now()
print("数据收集完毕，耗时：{0}".format(end-begin))


##########################将股票数据存入数据库###########################

#数据库名称和密码
name = 'root'
password = '123456'  #替换为自己的账户名和密码
#建立本地数据库连接(需要先开启数据库服务)
db = pymysql.connect('localhost', name, password, charset='utf8')
cursor = db.cursor()

#print(db_exists(cursor,"stockdatabase"))
#print(table_exists(cursor,"stock","stockdatabase"))
try:

    if db_exists(cursor,"stockdatabase")==False:
        sqlSentence1 = "create Database stockDataBase default charset utf8"
        cursor.execute(sqlSentence1)

    #选择使用当前数据库
    if table_exists(cursor,"stock","stockdatabase")==False:
        sqlSentence2 = "use stockDataBase;"
        cursor.execute(sqlSentence2)
        sqlSentence3 = "create table `stockDataBase`.`stock`(日期 date, 股票代码 VARCHAR(10),     名称 VARCHAR(10),\
                       收盘价 VARCHAR(10),    最高价    VARCHAR(10), 最低价 VARCHAR(10), 开盘价 VARCHAR(10), 前收盘 VARCHAR(10), 涨跌额    VARCHAR(10), \
                       涨跌幅 VARCHAR(10), 换手率 VARCHAR(10), 成交量 bigint, 成交金额 bigint, 总市值 bigint, 流通市值 bigint)"
        cursor.execute(sqlSentence3)
except Exception as e:
    print(e)


print("开始插入数据")
begin = datetime.datetime.now()
sqlSentence4 = "insert into stockDataBase.stock(日期, 股票代码, 名称, 收盘价, 最高价, 最低价, 开盘价, 前收盘, 涨跌额, 涨跌幅, 换手率,成交量, 成交金额, 总市值, 流通市值) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#获取的表中数据很乱，包含缺失值、Nnone、none等，插入数据库需要处理成空值
#sqlSentence4 = sqlSentence4.replace('nan','null').replace('None','null').replace('none','null')
try:
    cursor.executemany(sqlSentence4,stock_list)
except Exception as e:
    print(e)
end = datetime.datetime.now()
print("数据插入{0}条数据，耗时：{1}".format(len(stock_list),end-begin))
#关闭游标，提交，关闭数据库连接
cursor.close()
db.commit()
db.close()
