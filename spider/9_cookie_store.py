import  requests
import  json
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

# 把cookie存储为字典,requests.utils.dict_from_cookiejar()

cookie_dict=requests.utils.dict_from_cookiejar(session.cookies)

cookie_json=json.dumps(cookie_dict)

with open("cookie.txt",'w') as file:
    file.write(cookie_json)
    print(cookie_json,type(cookie_json))
