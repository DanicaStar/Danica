from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class TestCase():
    def __init__(self):
        self.driver = webdriver.Chrome()
        url = 'http://sahitest.com/demo/clicks.htm'
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        # self.ac=ActionChains(self.driver)

    def clear_data(self):     #该方法是清空动作的缓存
        for device in self.ac.w3c_actions.devices:
            device.actions.clear()


    def test_mouse(self):
        # 双击
        btn1 = self.driver.find_element_by_xpath('/html/body/form/input[2]')
        self.ac = ActionChains(self.driver)
        self.ac.double_click(btn1).perform()
        # self.clear_data()
        # sleep(2)

        # 单击
        btn2 = self.driver.find_element_by_xpath('/html/body/form/input[3]')
        self.ac = ActionChains(self.driver)
        self.ac.click(btn2).perform()
        # self.clear_data()
        # sleep(2)

        # 右击
        btn3 = self.driver.find_element_by_xpath('/html/body/form/input[4]')
        self.ac = ActionChains(self.driver)
        self.ac.context_click(btn3).perform()
        # self.clear_data()
        sleep(10)

    def keyboard(self):
        self.driver.get('http://www.baidu.com')
        kw = self.driver.find_element_by_id('kw')
        kw.send_keys('小丸子')
        kw.send_keys(Keys.BACKSPACE)   #回退删除1
        sleep(1)
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
    # case.test_mouse()
    case.keyboard()
