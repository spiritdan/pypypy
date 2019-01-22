from wxpy import *

bot = Bot(console_qr=True);
my_friend = bot.friends().search('spirit_dan', sex=MALE, city='苏州')[0]

my_friend.send('Hello, WeChat!')
