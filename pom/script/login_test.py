'''
login_test
封装业务层
调用page文件夹中的login_page.py
'''

from pom.page.login_page import LoginPage,login_url
from pom.common.base import open_browser

class TestLogin():
    def __init__(self):
        driver=open_browser()  #打开浏览器
        self.login=LoginPage(driver)   #实例化LoginPage
        self.login.open_url(login_url)   #打开登录地址

    #测试登录方法
    def test_login(self,username,password):
        #用例操作步骤
        #1、输入用户名
        self.login.input_username(username)
        #2、输入密码
        self.login.input_password(password)
        #3、点击记住密码
        self.login.click_remember()
        #4、点击登录按钮
        self.login.click_submit()
        #缺失预期结果

if __name__ == '__main__':
    login=TestLogin()
    login.test_login('Danica','123456')

