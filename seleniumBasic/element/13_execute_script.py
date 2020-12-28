from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    #获取alert
    def test1(self):
        js='alert("test")'
        self.driver.execute_script(js)
        sleep(2)
        self.driver.switch_to.alert.accept()

    #获取页面标题
    def test2(self):
        js = 'return document.title'
        title=self.driver.execute_script(js)
        print(title)

    #改变元素的样式
    def test3(self):
        js = 'var q=document.getElementById("kw");q.style.border="2px solid red"'
        self.driver.execute_script(js)

    #滚动条1
    def test4(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        self.driver.execute_script(js)

    # 滚动条2
    def test5(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        js_down = 'window.scrollTo(0,1000)'
        self.driver.execute_script(js_down)
        sleep(2)
        js_up = 'window.scrollTo(0,0)'
        self.driver.execute_script(js_up)

if __name__ == '__main__':
    case=TestCase()
    case.test5()
