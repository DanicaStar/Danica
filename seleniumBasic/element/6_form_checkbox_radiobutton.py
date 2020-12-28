import os
from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))    #获取当前文件夹路径
        file_path='file:///'+path+'/form_checkbox_radiobutton.html'
        self.driver.get(file_path)
    def test_checkBox(self):
        swimming=self.driver.find_element_by_id('swimming')
        if not swimming.is_selected():   #判断复选框是否选中
            swimming.click()   #选中复选框
        running=self.driver.find_element_by_id('running')
        if not running.is_selected():
            running.click()
        sleep(3)

    def test_radio(self):
        list_1=self.driver.find_element_by_name("gender")
        list_1.click()
        sleep(3)

    def test_submit(self):
        submit=self.driver.find_element_by_name('login')
        submit.click()
        sleep(3)

if __name__ == '__main__':
    case = TestCase()
    case.test_checkBox()
    case.test_radio()
    case.test_submit()