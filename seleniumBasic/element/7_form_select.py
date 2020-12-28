import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import  Select

class TestCase():
    def __init__(self):
        self.driver=webdriver.Chrome()
        path=os.path.dirname(os.path.abspath(__file__))    #获取当前文件夹路径
        file_path='file:///'+path+'/form_select.html'
        self.driver.get(file_path)
    def test_selct(self):
        se=self.driver.find_element_by_id('provice')
        select=Select(se)
        select.select_by_index(0)    #通过index来选择（从0开始）
        sleep(2)
        select.select_by_value('sz')   #通过选项中标签的value值选择
        sleep(2)
        select.select_by_visible_text('杭州')   #根据可视化文本来选择
        sleep(2)

    def test_selcts(self):
        se = self.driver.find_element_by_id('provice')
        select = Select(se)
        for i in range(2):
            select.select_by_index(i)
        sleep(2)
        select.deselect_all()   #反选
        sleep(2)
        self.driver.quit()

    def test_option(self):
        se = self.driver.find_element_by_id('provice')
        select = Select(se)
        for option in select.options:   #选中所有选项
            print(option.text)

if __name__ == '__main__':
    case = TestCase()
    case.test_option()