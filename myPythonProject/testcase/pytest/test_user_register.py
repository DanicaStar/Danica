# -*- coding:utf-8 -*-
# @Time : 2020-11-23 18:42
# @Author: Danica
# @File : test_user_register.py
from time import sleep
from selenium import  webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pythonProject.util import util
import pytest

class TestUserRegister(object):

    def setup_class(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()


    #测试注册，验证码错误
    def test_register_code_error(self):
        username='test001'
        email='test001@qq.com'
        pwd='123456'
        confirmPwd='123456'
        captcha='666'
        expected='验证码不正确'

        #输入用户名
        self.driver.find_element_by_name('username').send_keys(username)
        #输入邮箱
        self.driver.find_element_by_name('email').send_keys(email)
        #输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        #密码二次验证
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        #输入验证码
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        #点击注册按钮
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert

        #python的断言
        assert alert.text==expected
        alert.accept()    #点击弹框
        sleep(5)

    #测试注册成功
    def test_register_ok(self):
        username=util.gen_random_str()
        email=username+'@qq.com'
        pwd='123456'
        confirmPwd='123456'
        # 自动获取
        captcha=''
        expected='注册成功,点击确定进行登录'

        #输入用户名
        self.driver.find_element_by_name('username').clear()
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('email').clear()
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)

        captcha = util.get_code(self.driver, 'captchaimg')
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        self.driver.find_element_by_class_name('btn').click()

        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert

        #python的断言
        assert alert.text==expected
        alert.accept()
        sleep(5)

if __name__ == '__main__':
    pytest.main(['-sv','test_user_register.py'])