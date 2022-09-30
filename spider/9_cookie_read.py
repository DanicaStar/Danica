import  requests
import json
session=requests.session()  #创建一个session()对话的对象，帮助我们自动保存cookie
headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
try:
    cookie_txt=open('cookie.txt','r')
    cookie_dict=json.loads(cookie_txt.read())    #字符串转换为字典
    print(cookie_dict)
    print(type(cookie_dict))
    cookie=requests.utils.cookiejar_from_dict(cookie_dict)
    session.cookies=cookie
    comment_url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'
    comment_data = {
        'comment': input("请输入评论内容："),
        'submit': '发表评论',
        'comment_post_ID': '35',
        'comment_parent': ' 0'
    }
    comment_res = session.post(url=comment_url, headers=headers, data=comment_data)

except Exception as error:
    print("cooike文件不存在")
    login_url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
    login_data = {
        'log': ' kaikeba',
        'pwd': ' kaikeba888',
        'wp-submit': '登录',
        'redirect_to': ' https://xiaoke.kaikeba.com/example/wordpress/wp-admin/',
        'testcookie': ' 1'
    }
    login_res = session.post(url=login_url, headers=headers, data=login_data)
    cookie=session.cookies
    comment_url = 'https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'
    comment_data = {
        'comment': input("请输入评论内容："),
        'submit': '发表评论',
        'comment_post_ID': '35',
        'comment_parent': ' 0'
    }
    comment_res = session.post(url=comment_url, headers=headers, data=comment_data)
