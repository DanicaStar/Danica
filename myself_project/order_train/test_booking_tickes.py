# -*- coding:utf-8 -*-
# @Time : 2021-01-12 21:21
# @Author: Danica
# @File : test_booking_tickes.py
from myself_project.order_train.functions import functions
from myself_project.order_train.search_tickes import Search
class Book():
    def test_booking_tickes(self):
        Search.search_ticks(self,'杭州','合肥',3)
        functions.css(self,'body > div:nth-child(32) > div > div.lisBox > div.List-Box > div > div:nth-child(14) > div.w6 > div:nth-child(1) > a').click()

if __name__ == '__main__':
    book=Book()
    book.test_booking_tickes()