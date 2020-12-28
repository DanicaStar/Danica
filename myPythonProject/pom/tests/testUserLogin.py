# -*- coding:utf-8 -*-
# @Time : 2020-12-10 19:23
# @Author: Danica
# @File : testUserLogin.py
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from myPythonProject.pom.pages.userLoginPage import UserLoginPage

class TestUserLogin():
    login_data=[
        ('','123456','账号不能为空'),
        ('admin', '123456', '用户中心'),
    ]

    def setup_class(self):
        self.userLogin=UserLoginPage()

    @pytest.mark.parametrize('username,passwd,expected',login_data)
    def test_login(self,username,passwd,expected):
        self.userLogin.input_username(username)
        self.userLogin.input_pwd(passwd)
        self.userLogin.click_btn()

        if username=='':
            WebDriverWait(self.userLogin.driver, 5).until(EC.alert_is_present())
            alert = self.userLogin.driver.switch_to.alert
            sleep(2)

            assert alert.text==expected
            alert.accept()
            sleep(2)

        else:
            WebDriverWait(self.userLogin.driver, 5).until(EC.title_is(expected))
            sleep(2)
            assert self.userLogin.driver.title==expected
            sleep(2)

    # def tearDown_class(self):
        # self.userLogin.driver.quit()

if __name__ == '__main__':
    pytest.main(['-sv','testUserLogin.py'])

