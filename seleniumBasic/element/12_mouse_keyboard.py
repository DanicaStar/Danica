from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCase():
    def __init__(self):
        self.driver = webdriver.Chrome()
        url = 'http://sahitest.com/demo/clicks.htm'
        # self.driver.get(url)

    def test_mouse(self):
        # 双击
        btn = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        ActionChains(self.driver).double_click().perform()
        sleep(2)

        # 单击
        btn = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        ActionChains(self.driver).click().perform()
        sleep(2)

        # 右击
        btn = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        ActionChains(self.driver).context_click().perform()
        sleep(2)

    def keyboard(self):
        self.driver.get('http://www.baidu.com')
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys('小丸子')
        kw.send_keys(Keys.CONTROL, 'a')  # 全选
        sleep(2)
        kw.send_keys(Keys.CONTROL, 'x')  # 复制
        sleep(2)
        kw.send_keys(Keys.CONTROL, 'v')  # 黏贴
        sleep(2)

        ac = self.driver.find_element_by_class_name('pf')
        ActionChains(self.driver).move_to_element(ac).perform()
        sleep(2)


if __name__ == '__main__':
    case = TestCase()
    case.keyboard()
