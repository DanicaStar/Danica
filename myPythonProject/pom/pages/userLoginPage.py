# -*- coding:utf-8 -*-
# @Time : 2020-12-08 20:01
# @Author: Danica
# @File : userLoginPage.py
from selenium.webdriver.common.by import By
from  myPythonProject.pom.pages.basePage import BasePage
from time import sleep
class UserLoginPage(BasePage):
    username_input=(By.NAME,'user')
    pwd_input = (By.NAME, 'pwd')
    login_btn = (By.CLASS_NAME, 'btn')

    def __init__(self):
        url='http://localhost:8080/jpress/user/login'
        BasePage.__init__(self,url)

    def input_username(self,username):
        self.clear(*self.username_input)
        self.input_text(username,*self.username_input)

    def input_pwd(self,pwd):
        self.clear(*self.pwd_input)
        self.input_text(pwd,*self.pwd_input)

    def click_btn(self):
        self.click_element(*self.login_btn)
        sleep(2)



