# -*- coding:utf-8 -*-
# @Time : 2020-12-22 18:24
# @Author: Danica
# @File : userLogin.py

from selenium import webdriver
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUserLogin():
    def setup_class(self):
        self.driver=webdriver.Chrome()
        url='http://localhost:8080/jpress/user/login'
        self.driver.maximize_window()
        self.driver.get(url)

    data=[
        ('', '123456', '账号不能为空'),
        ('admin', '', '密码不能为空'),
        ('admin', '123455', '用户名或密码不正确'),
        ('join', '123456', '用户名不正确。'),
        ('join', '123455', '用户名不正确。'),
        ('admin', '123456', '用户中心'),
    ]
    @pytest.mark.parametrize('username,pwd,expected',data)
    def testLogin(self,username,pwd,expected):
        user=self.driver.find_element_by_name('user')
        user.clear()
        user.send_keys(username)
        passwd=self.driver.find_element_by_name('pwd')
        passwd.clear()
        passwd.send_keys(pwd)
        button=self.driver.find_element_by_class_name('btn')
        button.click()

        if username=='admin' and pwd=='123456':
            WebDriverWait(self.driver,5).until(EC.title_is(expected))
            assert self.driver.title==expected

        else:
            WebDriverWait(self.driver,5).until(EC.alert_is_present())
            alert=self.driver.switch_to.alert
            assert alert.text==expected
            alert.accept()

if __name__ == '__main__':
    if __name__ == '__main__':
        pytest.main(['-sv','userLogin.py'])





