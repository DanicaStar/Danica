'''
base.cy 对
selenium做二次封装
1、打开浏览器
2、输入网址
3、元素定位
4、元素操作

'''
from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def open_browser(browser='chrome'):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    elif browser=='ie':
        driver=webdriver.Ie()
    else:
        print("请输入正确的浏览器名称，如：chrome，firefox,ie")
        driver=None
    return driver

class Base:
    def __init__(self,driver):
        #初始化浏览器
        self.driver=driver

    def open_url(self,url):
        # 输入网址
        self.driver.get(url)
        # 浏览器最大化
        self.driver.maximize_window()
    def close(self):
        #关闭浏览器
        self.driver.quit()

    #单个元素定位
    def find_element(self,locator,timeout=10):
        #locator定位器，元组格式，例如（'id','id属性值'）
        try:
            element = WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            return element
        except:
            print(f'元素{locator}没有找到')
            return False

    #多个元素定位
    def find_elements(self, locator, timeout=10):
        #定位一组元素
        try:
            elements = WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
            return elements
        except:
            print(f'元素{locator}没有找到')
        return False

    #点击元素
    def click(self,locator):
        element=self.find_element(locator)
        try:
            element.click()
        except Exception as msg:
            print(msg)

    #文本输入
    def send_keys(self,locator,text):
        element=self.find_element(locator)
        try:
            element.clear()
            element.send_keys(text)
        except Exception as msg:
            print(msg)
    #点击空白处
    def click_blank(self):
        ActionChains(self.driver).move_by_offset(0, 0).click().perform()

    #判断文本是否在元素的文本中，如果在，返回True,不在，返回False
    def is_text_in_element(self,locator,text,timeout=10):
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    # 判断value值是否是元素value属性值对应的值，如果是，返回True,不是，返回False
    def is_value_in_element(self,locator,value,timeout=10):
        try:
            result=WebDriverWait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,value))
            return result
        except:
            return False

    #判断元素是否被选中，如果选中返回True，否则返回False
    def is_selected(self,locator):
        element=self.find_element(locator)
        try:
            result=element.is_selected()
            return  result
        except:
            return False
    #执行js,除去空间里面的'readonly'属性
    def js(self,element):   #通过selenium来执行JavaScript语句
        self.driver.execute_script("document.getElementById("+   "'"  +element+  "'"  +").removeAttribute('readonly')")


if __name__ == '__main__':
    driver=open_browser('chrome')
    base=Base(driver)
    base.open_url('http://www.baidu.com')
    # #搜索框定位器
    # search_loc=('id','kw')
    # #按钮定位器
    # button_loc = ('id','su')
    # #搜索框输入内容
    # base.send_keys(search_loc,'小丸子')
    # #点击"百度一下"
    # base.click(button_loc)
    new_loc=('link text','新闻')

    text='新闻'
    button_loc=('id','su')
    value='百度'
    print(base.is_text_in_element(new_loc, text))
    print(base.is_value_in_element(button_loc, value))



    time.sleep(2)
    base.close()
