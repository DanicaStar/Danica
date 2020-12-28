import  requests
session=requests.session()  #创建一个session()对话的对象，帮助我们自动保存cookie
login_url='https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
headers={
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
login_data={
    'log': ' kaikeba',
    'pwd': ' kaikeba888',
    'wp-submit': '登录',
    'redirect_to': ' https://xiaoke.kaikeba.com/example/wordpress/wp-admin/',
    'testcookie': ' 1'
}
login_res=session.post(url=login_url,headers=headers,data=login_data)
cookie=session.cookies

comment_url='https://xiaoke.kaikeba.com/example/wordpress/wp-comments-post.php'
comment_data={
    'comment': input("请输入评论内容："),
    'submit': '发表评论',
    'comment_post_ID': '35',
    'comment_parent': ' 0'
}
comment_res=session.post(url=comment_url,headers=headers,data=comment_data)
print(comment_res.status_code)