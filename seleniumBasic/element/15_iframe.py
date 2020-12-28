from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://sahitest.com/demo/framesTest.htm")

    def test1(self):
        first_frame=self.driver.find_element_by_name('top')
        #进入frame
        self.driver.switch_to.frame(first_frame)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[1]').click()
        sleep(2)
        #跳出当前的frame
        self.driver.switch_to.default_content()

        second_frame = self.driver.find_element_by_xpath('/html/frameset/frame[2]')
        self.driver.switch_to.frame(second_frame)
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[1]/a[2]').click()
        sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    case=TestCase()
    case.test1()