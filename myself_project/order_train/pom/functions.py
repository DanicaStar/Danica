# -*- coding:utf-8 -*-
# @Time : 2021-01-11 20:21
# @Author: Danica
# @File : functions.py

from selenium import webdriver
from datetime import datetime,date,timedelta
import xlrd,logging
from selenium.webdriver import ActionChains


class functions():
    def driver(self):
        self.driver=webdriver.Chrome()  #返回driver对象
        self.driver.maximize_window()  # 通过driver设置打开协程火车票网站
        return self.driver

    def get_url(self,url):   #打开协程火车票首页面
        self.driver.get(url)

    def arrive_time(self, n):  #将返回n天后日期
        return str((date.today() + timedelta(days=int(n))).strftime("%Y-%m-%d"))

    def id(self,element):
        return self.driver.find_element_by_id(element)

    def class_name(self,element):
        return self.driver.find_element_by_class_name(element)

    def css(self,element):
        return self.driver.find_element_by_css_selector(element)

    def js(self,element_id):   #通过selenium来执行JavaScript语句
        self.driver.execute_script("document.getElementById("+   "'"  +element_id+  "'"  +").removeAttribute('readonly')")

    def click_bank(self):   #点击空白处
        ActionChains(self.driver).move_by_offset(0,0).click().perform()

    def read_excel(self,filename,index):
        wb=xlrd.open_workbook(filename)
        sheet=wb.sheet_by_index(index)
        rows=sheet.nrows
        cols=sheet.ncols
        dic= {}
        for i in range(rows):
            data=[]
            for j in range(cols):
                data.append(sheet.col_values(j)[i])
            dic[i]=data
        return dic


    def log(self, str):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s %(filename)s %(levelname)s %(message)%',
            datefmt='%a,%d %b %Y %H:%M:%S',
            filename='../booking.log',
            filemode='a'
        )
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        logging.info(str)

if __name__ == '__main__':
    test=functions()
    print(test.read_excel('station.xlsx', 0))
