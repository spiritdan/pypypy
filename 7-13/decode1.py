print('枫'.encode('gbk'))
#将汉字'枫'使用gbk编码，得到：b'\xb7\xe3'
print(b'\xb7\xe3'.decode('gbk'))
#解码，得到：枫
print('枫'.encode('utf-8'))
#将汉字'枫'使用utf-8编码，得到：b'\xe6\x9e\xab'
print(b'\xe6\x9e\xab'.decode('utf-8'))
#解码，得到：枫
print('吴枫'.encode('utf-8'))
print('吴枫'.encode('gbk'))
print('ABC'.encode('ASCII'))
print(b'\xce\xe2\xb7\xe3'.decode('gbk'))


print(ord('枫'))
#得到的结果会是26539，这是用十进制表示的数。
print(chr(26539))
#chr()的用法和ord()的用法是恰好相反的，可以把整数编码，变成汉字。

#我们也可以把它转为16进制，结果是：67ab。 \u表示16进制
print('\u67ab')


