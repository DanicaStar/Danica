# 分析
"""
在我们的博客网站中有一篇加密文章，需要输入密码才能看到内容，加密密码是 xiaoke123
内容是包含在一个 class = "entry-content" 中
通过爬虫输入密码之后爬到文章内容！
"""
import requests
from bs4 import BeautifulSoup


post_url = 'https://xiaoke.kaikeba.com/example/wordpress/2019/11/07/互联网圈炸锅啦！有人要帮你加薪啦！/'   #文章的URL
url_login = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php?action=postpass'         #登录页面，需要密码
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
session=requests.session()

login_params={
    'post_password': 'xiaoke123',
    'Submit': '提交'
}

login_res=session.post(url=url_login,headers=headers,data=login_params)

def get_text():
    text_res=session.get(url=post_url,headers=headers)
    soup=BeautifulSoup(text_res.text,'html.parser')
    post_content=soup.find('div', class_='entry-content')
    if (post_content is None):
        print('没有内容')
    else:
        print(post_content.text)

get_text()