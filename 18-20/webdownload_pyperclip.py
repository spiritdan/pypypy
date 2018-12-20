'''
借助副本学习pyperclip和webbrowser模块的用法，学习如何双击运行程序的方法，实现一键下载电影。
注：网页系统不支持pyperclip和webbrowser模块，该挑战需要你在自己的本地电脑上完成。在此你只需要print('我已完成该挑战')，执行并提交即可。
https://shimo.im/docs/t1HAyUMCp6QR3Fv3/

'''
import webbrowser,pyperclip
from urllib.request import quote
#引用webbrowser,pyperclip模块。如果是在本地电脑运行，要先安装pyperclip模块。方法是在终端里运行pip install pyperclip
item = pyperclip.paste()
utfitem=item.encode('utf-8')
#将粘贴板中的内容“海边的卡夫卡”，赋值给item
webbrowser.open('https://book.douban.com/subject_search?search_text='+quote(utfitem)+'&cat=1001')
#打开网址https://book.douban.com/subject_search?search_text=海边的卡夫卡&cat=1001
