# -*- coding:utf-8 -*-
# @Time : 2020-12-08 20:15
# @Author: Danica
# @File : testUserRegister.py

from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from pom import util
import pytest
from pom.pages.userRegisterPage import UserRegisterPage


class TestUserRegister():
    register_data = [
        ('test001', 'test001@qq.com', '123456', '123456', '666', '验证码不正确'),
        ('test002', 'test002@qq.com', '123456', '123456', '111', '注册成功，点击确定进行登录')

    ]

    def setup_class(self):
        self.registerPage=UserRegisterPage()

    @pytest.mark.parametrize('username,email,pwd,confirmPwd,captcha,expected',register_data)
    def test_register(self,username,email,pwd,confirmPwd,captcha,expected):

        #输入用户名
        self.registerPage.input_username(username)
        #输入邮箱
        self.registerPage.input_email(email)
        #输入密码
        self.registerPage.input_pwd(pwd)
        #密码二次验证
        self.registerPage.input_confirmPwd(confirmPwd)

        #自动识别验证码
        if captcha !='666':
            captcha=util.get_code(self.registerPage.driver,'captchaimg')

            #输入验证码
            self.registerPage.input_captcha(captcha)

            # 点击注册按钮
            self.registerPage.click_btn()

            #等待alert出现
            WebDriverWait(self.registerPage.driver,5).until(EC.alert_is_present())
            alert=self.registerPage.driver.switch_to.alert

            #python的断言
            assert alert.text==expected
            alert.accept()    #点击弹框
            sleep(2)
        else:
            self.registerPage.input_captcha(captcha)
            self.registerPage.click_btn()

            WebDriverWait(self.registerPage.driver,5).until(EC.alert_is_present())
            alert=self.registerPage.driver.switch_to.alert

            assert alert.text==expected
            alert.accept()    #点击弹框
            sleep(2)

    def tearDown_clas(self):
        self.registerPage.driver.quit()
if __name__ == '__main__':
    pytest.main(['-sv', 'testUserRegister.py'])

