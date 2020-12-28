import schedule
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header


def func():
    return '今天阳光明媚'

def send_email(content,sender,pwd,recevier):
    #右键服务器
    mailhost='smtp.qq.com'
    qqmail=smtplib.SMTP()
    qqmail.connect(mailhost,25)  #端口
    qqmail.login(sender,pwd)

    #发送内容
    content="今天的天气是："+content
    message=MIMEText(content,'plain','utf-8')

    #主题
    subject='今日天气预报'
    message['subject']=Header(subject,'utf-8')

    try:
        qqmail.sendmail(sender,recevier,message.as_string())
        return True
    except:
        qqmail.quit()

def job():
    print('开始第一次发送任务')
    data=func()
    sender=input("请输入发件人的邮箱账号：")
    pwd=input("请输入发件人的邮箱密码：")
    recevier = input("请输入收件人邮箱账号：")

    IsSuccess=send_email(data,sender,pwd,recevier)
    while IsSuccess is False:
        print("邮件发送失败，正在尝试重新发送")
        IsSuccess=send_email(data,sender,pwd,recevier)
    print('任务完成')

# 设置定时
schedule.every(0.1).minutes.do(job)  #每隔{}分钟，执行一次job函数
# schedule.every().day.at('19:20').do(job)
while True:
    schedule.run_pending()
    time.sleep(1)