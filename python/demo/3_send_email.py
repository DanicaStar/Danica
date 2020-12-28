from email import encoders   #encoders模块负责编码
from email.header import Header    #Header模块负责处理邮件头
from email.mime.text import MIMEText    #MIMEText模块负责处理文本
from email.utils import parseaddr, formataddr   #parseaddr模块与formataddr模块 负责将输入的内容格式化
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( Header(name, 'utf-8').encode(), addr))

#输入Email地址和口令
from_addr=input (" 请输入发件人的邮箱号码Form：")
password=input (" 请输入发件人的邮箱密码Password：")
#输入SMTP服务器地址
smtp_server=input("请输入邮箱服务器地址smtp_server")
#输入收件人地址
to_addr=[]
while True:
    to_addr.append(input("请输入收件人地址to_addr:"))
    answer=input("是否继续输入邮箱地址(y/n)")
    if answer=="y":
        continue
    else:
        break
msg = MIMEText('hello world', 'plain', 'utf-8')
msg['From'] = _format_addr(u'python <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自小星的问候……', 'utf-8').encode()

server=smtplib.SMTP_SSL(smtp_server,465)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
print("发送成功")
server.quit()






