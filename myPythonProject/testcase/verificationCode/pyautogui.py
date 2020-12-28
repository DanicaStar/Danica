# -*- coding:utf-8 -*-
# @Time : 2020-12-03 19:57
# @Author: Danica
# @File : pyautogui.py
from selenium import webdriver
import pyautogui
from time import sleep
driver=webdriver.Chrome()
url='http://www.jpress.io/user/register'
driver.get(url)
driver.maximize_window()


element=driver.find_element_by_id('agree')
rect=element.rect
pyautogui.click(rect['x']+10,rect['y']+130)
sleep(3)