#coding=gbk
from urllib.request import quote,unquote

print(quote('ˮ������'.encode('gbk')))
print(quote('ˮ������'))
print(quote('ˮ������'.encode('utf8')))