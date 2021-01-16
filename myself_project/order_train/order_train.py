# -*- coding:utf-8 -*-
# @Time : 2021-01-07 20:06
# @Author: Danica
# @File : order_train.py
from selenium import webdriver
from time import sleep
import time
from datetime import datetime,date,timedelta

from selenium.webdriver import ActionChains


def date_n(n):
    return str((date.today()+timedelta(days=+int(n))).strftime('%Y-%m-%d'))
from_station='杭州'
arrive_station='合肥'
tommorrow=date_n(1)
print(tommorrow)

url='https://trains.ctrip.com/'
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)


#出发城市
driver.find_element_by_id('departCityName').send_keys(from_station)
sleep(1)
#到达城市
driver.find_element_by_id('arriveCityName').send_keys(arrive_station)
sleep(1)
#移除出发时间的’readonly‘属性
driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
#出发时间
departDate=driver.find_element_by_id('departDate')
departDate.clear()
departDate.send_keys(tommorrow)
sleep(1)

#为了解决日期控件弹出框在输入日期后无法消失的问题，要让鼠标单击一下页面的空白处
ActionChains(driver).move_by_offset(0,0).click().perform()


#开始搜索
searchbtn=driver.find_element_by_class_name('searchbtn')
searchbtn.click()
sleep(1)

#选择G7674班次的二等座
driver.find_element_by_css_selector('body > div:nth-child(32) > div > div.lisBox > div.List-Box > div > div:nth-child(14) > div.w6 > div:nth-child(1) > a').click()
sleep(3)
driver.find_element_by_class_name('input-name').send_keys('小丸子')


#注意的点：
# 1、日期弹框可能无法输入，要考虑JavaScrip来消除日期选框的readonly
# 2、输入日期后，日期弹框无法消失，要单击页面的空白处

