import time
import datetime
st="8:00:00"

def string_toDatetime(st,min):
    dt= datetime.datetime.strptime(st, "%H:%M:%S")
    #print(dt)
    new_dt=dt+ datetime.timedelta(seconds=int('+{0}'.format(min)))
    str_dt=new_dt.strftime("%H:%M:%S")
    print('随机到：',str_dt,'开始')
    return str_dt



string_toDatetime(st,240)
a=[1,2,3,4,5,6]
for key,value in enumerate(a):
    print(key,value)
