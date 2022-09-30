import requests
from bs4 import  BeautifulSoup
import schedule
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header

count=0
def func():
    url='http://www.weather.com.cn/weather/101211001.shtml'
    headers={
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    res=requests.get(url=url,headers=headers)
    res.encoding = 'utf-8'
    if res.status_code==200:

        soup=BeautifulSoup(res.text,'html.parser')
        weather=soup.find('p',class_="wea").text
        tempreture=soup.find('p',class_="tem").text
        return weather,tempreture

    else:
        print("请求失败")

def send_email(weather,tempreture,sender,pwd,recevier):
    #右键服务器
    mailhost='smtp.qq.com'
    qqmail=smtplib.SMTP()
    qqmail.connect(mailhost,25)  #端口
    qqmail.login(sender,pwd)

    #发送内容
    content='衢州的天气是：\n'+weather+tempreture
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
    global count
    print('开始第一次发送任务')
    weather,tempreture=func()
    sender=input("请输入发件人的邮箱账号：")
    pwd=input("请输入发件人的邮箱账户授权码：")
    recevier = input("请输入收件人邮箱账号：")

    IsSuccess=send_email(weather,tempreture,sender,pwd,recevier)
    while IsSuccess is False:
        print("邮件发送失败，正在尝试重新发送")
        IsSuccess=send_email(weather,tempreture,sender,pwd,recevier)
    print('任务完成')
    count+=1

# 设置定时
schedule.every(1).seconds.do(job)  #每隔{}分钟，执行一次job函数
# schedule.every().day.at('19:20').do(job)
while count<2:
    schedule.run_pending()
    time.sleep(1)