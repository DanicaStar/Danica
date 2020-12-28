# -*- coding:utf-8 -*-
# @Time : 2020-12-22 15:26
# @Author: Danica
# @File : userlogin_myself.py

import pytest
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestUserLogin():
    def setup_class(self):
        self.driver = webdriver.Chrome()
        url = 'http://localhost:8080/jpress/user/login'
        self.driver.maximize_window()
        self.driver.get(url)
        return self.driver

    data=[
        ('','123456','账号不能为空'),
        ('admin','','密码不能为空'),
        ('admin','123455','用户名或密码不正确'),
        ('join','123456','用户名不正确。'),
        ('join','123455','用户名不正确。'),
        ('admin','123456','用户中心'),
    ]

    def tearDown_class(self):
        # sleep(2)
        self.driver.quit()


    @pytest.mark.parametrize('users,pwd,expected',data)
    def test_login(self,users,pwd,expected):

        user=self.driver.find_element_by_name('user')
        user.clear()
        user.send_keys(users)
        passwd=self.driver.find_element_by_name('pwd')
        passwd.clear()
        passwd.send_keys(pwd)
        self.driver.find_element_by_class_name('btn').click()

        if users=='admin' and pwd=='123456':
            WebDriverWait(self.driver,5).until(EC.title_is(expected))
            assert self.driver.title==expected
            # sleep(3)

        else:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            # sleep(2)
            assert alert.text==expected
            alert.accept()



        # here=self.driver.find_element_by_css_selector('.help-block>a')
if __name__ == '__main__':
    pytest.main(['-sv', 'userlogin_myself.py'])
