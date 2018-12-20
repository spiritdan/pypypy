#coding=gbk
from urllib.request import quote,unquote

print(quote('水形物语'.encode('gbk')))
print(quote('水形物语'))
print(quote('水形物语'.encode('utf8')))