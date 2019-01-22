import pymysql.cursors

sql="select *  from table"
connect=pymysql.Connect(
    host='',
    port=1521,
    db='utf8',
    user='user',
    passwd='123')
cursor = connect.cursor()
try:
    cursor.execute(sql)
except Exception as e:
    connect.rollback()
else:
    connect.commit()
