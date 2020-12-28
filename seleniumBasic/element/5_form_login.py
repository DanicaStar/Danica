import os
from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))    #获取当前文件夹路径,abspath(__file__)获取当前文件
        file_path='file:///'+path+'/form_login.html'
        self.driver.get(file_path)

    def test_login(self):
        username=self.driver.find_element_by_id('username')
        username.send_keys('admin')
        pwd=self.driver.find_element_by_id('pwd')
        pwd.send_keys('123')

        print(username.get_attribute('value'))   #获取用户名的值

        sleep(1)
        self.driver.find_element_by_id('submit').click()   #提交
        self.driver.switch_to.alert.accept()      #关闭alert
        username.clear()     #清空用户名
        sleep(1)
        self.driver.quit()


if __name__ == '__main__':
    case = TestCase()
    case.test_login()