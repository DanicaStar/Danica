# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 5:52 下午
# @Author  : danica
# @FileName: base.py
# @Software: PyCharm

"""
浏览器的基础操作
    1.浏览器打开方式 

    2.打开被测网址 
    3.封装元素定位方法 
    4.封装元素操作方法 
        4.1点击 
        4.2输入 
    5.判断元素是否存在 
    6.关闭浏览器 
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def open_browser(browser="Chrome"):
    if browser == 'Chrome':
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "Ie":
        driver = webdriver.Ie()
    else:
        print("请输入正确的浏览器: Chrome, Firefox, Ie")
        return False
    return driver


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        # 输入网址
        self.driver.get(url)
        # 浏览器最大化
        self.driver.maximize_window()

    def find_element(self, locator, timeout=10):
        """
        查找页面元素
        :param locator: 页面元素的定位方式 元素 : ("id", "id的属性值")
        :param timeout: 查找页面元素的等待时间
        :return: 成功: 返回定位的页面元素, 失败:False
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            print(f"元素{locator}没有找到:", e)
            return False

    def click(self, locator, timeout=10):
        """
        点击元素
        :param locator: 元素定位器
        :param timeout:
        :return:
        """
        element = self.find_element(locator, timeout)  # 先查找元素
        element.click()  # 再点击元素

    def send_keys(self, locator, text, timeout=10):
        """
        元素输入值
        :param locator:
        :param text: 输入的文本
        :param timeout:
        :return:
        """
        try:
            element = self.find_element(locator, timeout)  # 先定位
            element.clear()  # 清空
            element.send_keys(text)  # 再输入
        except Exception as e:
            print(f"元素{locator}没有找到:", e)

    def select_value(self, locator, value):
        """
        根据value值选择下拉框的选项值
        :param locator:
        :param value:
        :return:
        """
        select = Select(self.find_element(locator))
        select.select_by_value(value)

    def select_index(self, locator, index):
        """
        根据索引来选择下拉框的选项值
        :param locator:
        :param index:
        :return:
        """
        select = Select(self.find_element(locator))
        select.select_by_index(index)

    def element_selected(self, locator, timeout=10):
        """
        选择选择，如果元素未选择，则选中，否则不做操作
        :param locator:
        :param timeout:
        :return:
        """
        # 定位
        try:
            element = self.find_element(locator, timeout)
            if not element.is_selected():
                element.click()
        except Exception as e:
            print(f"元素{locator}没有找到:", e)

    def quit(self):
        self.driver.quit()

    def is_text_in_element(self, locator, text, timeout=10):
        """
        判断文本是否在元素的文本中，如果在则返回True,否则返回False
        :param locator:  元素定位器
        :param text: 要比较的文本
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, text, timeout=10):
        """
        判断value是否在元素的文本中，如果在则返回True,否则返回False
        :param locator:  元素定位器
        :param text: 要比较的文本
        :param timeout:
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, text))
            return result
        except:
            return False


if __name__ == '__main__':
    url = "http://www.baidu.com"
    driver = open_browser()
    base = Base(driver)
    base.open_url(url)
    input_loc = ('id', 'kw')
    button_loc = ('id', 'su')
    new_loc = ('link text', '新闻')
    print(base.is_value_in_element(button_loc, '百度一下'))
    print(base.is_text_in_element(new_loc, '新闻'))
    base.quit()
