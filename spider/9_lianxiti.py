'''
利⽤session实现发布⾖瓣读书个⼈中⼼⽣活点滴
使⽤技术点  requests请求  session会话  cookie参数
'''
import  requests
session=requests.session()  #创建一个session()对话的对象，帮助我们自动保存cookie
url='https://www.douban.com/'
headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
login_data={
    'channel': 'notification:user:161495576',
    'auth': '161495576_1598711999:d3f4757988bf7121ecc0dad239f996420f8a9fd6'
}
login_res=session.post(url=url,headers=headers,data=login_data)
cookie=session.cookies
print(cookie)
comment=input('请输入发布内容：')
comment_data={
'ck': '1V_V',
'comment': comment,
'privacy_and_reply_limit': 'P'
}
comment_res=session.post(url=url,headers=headers,data=comment_data)
print(comment_res.status_code)