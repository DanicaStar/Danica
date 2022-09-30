# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 6:48 下午
# @Author  : danica
# @FileName: login_page.py
# @Software: PyCharm


"""
定位元素方法和操作元素方法，元素定位全部放一起，每一个操作元素动作写成一个方法 
"""
from web_selenium.common.base import Base, open_browser

login_url = "http://ecshop.itsoso.cn/user.php"


class LoginPage(Base):
    # 定位元素方法
    username_loc = ('name', "username")  # 用户名的输入框
    password_loc = ('name', "password")  # 密码的输入框
    remember_loc = ('id', "remember")  # 记住密码按钮
    submit_loc = ('name', "submit")  # 登陆按钮

    # 操作元素方法，每个元素的操作都写成一个方法
    def input_username(self, username):
        # 输入用户名
        self.send_keys(self.username_loc, username)

    def input_password(self, password):
        # 输入密码
        self.send_keys(self.password_loc, password)

    def click_remember(self):
        # 勾选记住密码弹框
        self.element_selected(self.remember_loc)

    def click_submit(self):
        # 点击登陆按钮
        self.click(self.submit_loc)


if __name__ == '__main__':
    # 登陆流程
    driver = open_browser()
    login = LoginPage(driver)
    login.open_url(login_url)
    login.input_username("danica")
    login.input_password("123456")
    login.click_remember()
    login.click_submit()
    login.quit()
