import smtplib, time
from email.mime.text import MIMEText
from email.header import Header

file = open('./chengji.txt', 'r', encoding='utf8')
score = file.readlines()
file.close
# print(score)
mail_dict = {}

temp_mail = []
temp_course = []
temp_score = []

[temp_mail.append(score[i].strip('\n')) for i in range(0, len(score), 3)]
[temp_course.append(score[i].strip('\n')) for i in range(1, len(score), 3)]
[temp_score.append(score[i].strip('\n')) for i in range(2, len(score), 3)]

for i in range(0,len(temp_score)):
    mail_dict[temp_mail[i]] = temp_course[i] + temp_score[i]
print(mail_dict)


qqmail = smtplib.SMTP_SSL('smtp.qq.com', 465)


def sendmail(text, recipient, account, password):
    qqmail.login(account, password)
    # 以上，是登录邮箱
    theme = '考试成绩'

    sender = 'william'
    # 以上，是输入内容
    message = MIMEText(text, 'plain', 'utf-8')
    message['Subject'] = Header(theme, 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    # 以上，是一波转换操作

    try:
        qqmail.sendmail(account, recipient, message.as_string())
        print(recipient + '邮件已发送')
    except:
        print('对不起，发送失败请重试！')
    # 以上，是发送


#account = input('请输入你的QQ邮箱：')
#password = input('请输入你的邮箱密码：')

for key, value in mail_dict.items():
    text = value
    recipient = key
    print(recipient)
    print(text)
    #sendmail(text, recipient, account, password)
    #time.sleep(30)

#qqmail.quit()
print('全部邮件已完成发送')