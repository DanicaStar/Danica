# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 6:16 下午
# @Author  : danica
# @FileName: test_fore.py
# @Software: PyCharm


import requests

# 注册接口
login_url = 'http://register'
register_data = {'username': '小丸子', 'password': '123'}
r_register = requests.post(url=login_url, data=register_data)
print(r_register.text)
print(r_register.status_code)

# 登陆接口
login_url = 'http://login'
login_json = {'username': '小丸子', 'password': '123'}
r_login = requests.post(url=login_url, json=login_json)
print(r_login.json())
print(r_login.status_code)
