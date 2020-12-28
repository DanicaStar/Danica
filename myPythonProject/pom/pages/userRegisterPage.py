# -*- coding:utf-8 -*-
# @Time : 2020-12-08 19:38
# @Author: Danica
# @File : userRegisterPage.py

from time import sleep
from selenium.webdriver.common.by import By
from pom.pages.basePage import BasePage


class UserRegisterPage(BasePage):
    username_input = (By.NAME, 'username')
    email_input = (By.NAME, 'email')
    pwd_input = (By.NAME, 'pwd')
    confirmPwd_input = (By.NAME, 'confirmPwd')
    captcha_input = (By.NAME, 'captcha')
    register_btn = (By.CLASS_NAME, 'btn')

    def __init__(self):
        url = 'http://localhost:8080/jpress/user/register'
        BasePage.__init__(self, url)

    def input_username(self, username):
        self.clear(*self.username_input)
        self.input_text(username, *self.username_input)

    def input_email(self, email):
        self.clear(*self.email_input)
        self.input_text(email, *self.email_input)

    def input_pwd(self, pwd):
        self.clear(*self.pwd_input)
        self.input_text(pwd, *self.pwd_input)

    def input_confirmPwd(self, confirmPwd):
        self.clear(*self.confirmPwd_input)
        self.input_text(confirmPwd, *self.confirmPwd_input)

    def input_captcha(self, captcha):
        self.clear(*self.captcha_input)
        self.input_text(captcha, *self.captcha_input)

    def click_btn(self):
        self.click_element(*self.register_btn)
        sleep(2)
