from selenium import webdriver
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        path='file:///'+os.path.abspath('test_wait.html')
        self.driver.get(path)

    def test(self):
        self.driver.find_element_by_id('btn').click()
        #显示等待
        web=WebDriverWait(self.driver,1)
        loc=(By.ID,'id2')
        web.until(EC.text_to_be_present_in_element(loc,'id 2'))
        print(self.driver.find_element_by_id('id2').text)
        print('ok')

if __name__ == '__main__':
            case = TestCase()
            case.test()