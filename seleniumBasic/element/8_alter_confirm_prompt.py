import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import  Select

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))    #获取当前文件夹路径
        file_path='file:///'+path+'/alter_confirm_prompt.html'
        self.driver.get(file_path)
    def test_alert(self):
        self.driver.find_element_by_id('alert').click()
        alert=self.driver.switch_to.alert
        print(alert.text)
        sleep(3)
        alert.accept()

    def test_confirm(self):
        self.driver.find_element_by_id('comfirm').click()
        comfirm=self.driver.switch_to.alert
        print(comfirm.text)
        comfirm.accept()    #确定
        sleep(3)
        comfirm.dismiss()    #取消


    def test_prompt(self):
        self.driver.find_element_by_id('prompt').click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        prompt.accept()


if __name__ == '__main__':
    case = TestCase()
    # case.test_alert()
    # case.test_confirm()
    case.test_prompt()