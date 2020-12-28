from selenium import webdriver
from time import sleep
class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.maximize_window()
        sleep(1)

    def test_id(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        sleep(1)
        self.driver.find_element_by_id('su').click()
        sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    case=TestCase()
    case.test_id()






