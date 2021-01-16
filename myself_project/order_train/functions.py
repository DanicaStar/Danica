# -*- coding:utf-8 -*-
# @Time : 2021-01-11 20:21
# @Author: Danica
# @File : functions.py

from selenium import webdriver
from datetime import datetime,date,timedelta
import xlrd,logging

class functions():
    def driver(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        return self.driver

    def get_url(self,url):
        self.driver.get(url)

    def arrive_time(self, n):
        return str((date.today() + timedelta(days=int(n))).strftime("%Y-%m-%d"))

    def id(self,element):
        return self.driver.find_element_by_id(element)

    def class_name(self,element):
        return self.driver.find_element_by_class_name(element)

    def css(self,element):
        return self.driver.find_element_by_css_selector(element)

    def js(self,element):
        self.driver.execute_script("document.getElementById("+   "'"  +element+  "'"  +").removeAttribute('readonly')")

    def read_excel(self,filename,index):
        pass

