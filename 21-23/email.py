import smtplib
from email.mime.text import MIMEText
from email.header import Header
from sys import exit

qqmail = smtplib.SMTP_SSL('smtp.qq.com', 465)
account = input('请输入你的QQ邮箱：')
password = input('请输入你的邮箱密码：')
try:
    qqmail.login(account, password)
except:
    print('密码错误')
    exit()

theme = input('请输入邮件标题：')
text = input('请输入邮件正文，使用换行：')
recipient = input('请输入收件人邮箱，多个发件人使用空格隔开：')
recipient = recipient.split()
sender = input('请输入发件人昵称（可跳过）：')

message = MIMEText(text, 'plain', 'utf-8')
message['Subject'] = Header(theme, 'utf-8')
message['From'] = Header(sender, 'utf-8')

try:
    qqmail.sendmail(account, recipient, message.as_string())
except:
    print('对不起，发送失败请重试！')

qqmail.quit()