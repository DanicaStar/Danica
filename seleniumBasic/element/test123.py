# # -*- coding:utf-8 -*-
# # @Time : 2020-12-29 20:29
# # @Author: Danica
# # @File : test123.py
from time import sleep
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

url='https://user.qunar.com/passport/login.jsp?'
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.find_element_by_class_name('pwd-login').click()
driver.save_screenshot('page.png')
code=driver.find_element_by_id('vcodeImg')
left=code.location['x']
top=code.location['y']
right=left+code.size['width']
bottom=top+code.size['height']
img=Image.open('page.png')
img=img.crop((left,top,right,bottom))
img.save('t.png')


