import os,time
from selenium import webdriver
from time import sleep

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test1(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        self.driver.find_element_by_id('su').click()
        sleep(2)
        #截屏放到当前目录下
        self.driver.save_screenshot('小丸子.png')

    # 截屏以时间命名
    def test2(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        self.driver.find_element_by_id('su').click()
        st= time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        file_name=st+'.png'
        self.driver.save_screenshot(file_name)

    # 截屏放到指定的文件夹
    def test3(self):
        self.driver.find_element_by_id('kw').send_keys('小丸子')
        self.driver.find_element_by_id('su').click()
        st= time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        file_name = st + '.png'
        path=os.path.abspath("screenshot")    #要在当前文件路径下建立文件夹screenshot
        file_path=path+'/'+file_name
        self.driver.get_screenshot_as_file(file_path)
        self.driver.quit()
if __name__ == '__main__':
    case=TestCase()
    case.test3()