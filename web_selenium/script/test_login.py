# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 7:05 下午
# @Author  : danica
# @FileName: test_login1.py
# @Software: PyCharm


from web_selenium.page.login_page import LoginPage, login_url
from web_selenium.common.base import open_browser


class TestLogin(LoginPage):
    def __init__(self):
        driver = open_browser()
        self.login = LoginPage(driver)
        self.open_url(login_url)

    def test_login(self, username, password):
        """
        测试登陆的方法
        用例的操作步骤
        """
        # 输入用户名
        self.login.input_username(username)
        # 输入密码
        self.login.input_password(password)
        # 点击记住密码弹框
        self.login.click_remember()
        # 点击登陆按钮
        self.login.click_submit()
        # 关闭浏览器
        self.quit()


if __name__ == '__main__':
    test = TestLogin()
    test.test_login('danica', '123456')
