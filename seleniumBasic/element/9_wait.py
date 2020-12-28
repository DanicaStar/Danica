from selenium import webdriver
from time import  sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        url='http://www.baidu.com'
        self.driver.get(url)

    def test_sleep(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        sleep(2)
        self.driver.quit()

    def test_implicitly_wait(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        self.driver.quit()
        sleep(2)

    def test_webdriver_wait(self):
        wait=WebDriverWait(self.driver,2)
        wait.until(EC.title_is('百度一下，你就知道'))
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        sleep(2)
        self.driver.find_element_by_id('su').click()
        self.driver.quit()
        sleep(2)

if __name__ == '__main__':
    case=TestCase()
    # case.test_sleep()
    case.test_implicitly_wait()
    case.test_webdriver_wai()