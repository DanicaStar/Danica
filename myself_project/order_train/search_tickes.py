# -*- coding:utf-8 -*-
# @Time : 2021-01-12 21:04
# @Author: Danica
# @File : search_tickes.py
from selenium.webdriver import ActionChains
from time import sleep
from myself_project.order_train.functions import functions

class Search():
    def search_ticks(self,from_station,arrive_station,n):
        driver=functions.driver(self)
        url='https://trains.ctrip.com/'
        functions.get_url(self,url)
        functions.id(self,'departCityName').send_keys(from_station)
        sleep(2)
        functions.id(self,'arriveCityName').send_keys(arrive_station)
        sleep(2)

        functions.js(self,'departDate')
        departDate=functions.id(self,'departDate')
        departDate.clear()
        arrive_time=functions.arrive_time(self,n)
        departDate.send_keys(arrive_time)

        ActionChains(driver).move_by_offset(0,0).click().perform()
        functions.class_name(self,'searchbtn').click()


