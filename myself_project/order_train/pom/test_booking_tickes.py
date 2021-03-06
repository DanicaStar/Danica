# -*- coding:utf-8 -*-
# @Time : 2021-01-12 21:21
# @Author: Danica
# @File : test_booking_tickes.py
# from myself_project.order_train.pom.functions import  functions
# from myself_project.order_train.pom.search_tickes  import Search
# class Book():
#     def test_booking_tickes(self):
#         Search.search_ticks(self,'杭州','合肥',3)
#         functions.css(self,'body > div:nth-child(32) > div > div.lisBox > div.List-Box > div > div:nth-child(14) > div.w6 > div:nth-child(1) > a').click()
#
# if __name__ == '__main__':
#     book=Book()
#     book.test_booking_tickes()
#


from myself_project.order_train.pom.functions import functions
from myself_project.order_train.pom.search_tickes import Search
import time
# import HTMLTestRunner
import unittest
#
# class Booking_tickes(unittest.TestCase):
#     def setUp(self):
#         self.driver = functions.driver(self)
#     def test_ctrip_tickes(self):
#         functions.log(self,'Read Excel Files to get test data.')
#         dic1=functions.read_excel(self,'station.xlsx',0)
#         print(self,dic1[0][0],dic1[0][1])
#
#         functions.log(self, 'Begin to search tickes.')
#         Search.search_ticks(self, dic1[0][0], dic1[0][1], 1)
#         functions.log(self, 'End to search tickes.')
#         functions.log(self,"Begin to get driver object")
#         self.driver=functions.driver(self)
#
#         time.sleep(2)  #在页面跳转时加上时间等待，避免元素定位出现异常
#         functions.log(self, 'Click book button:)')
#         functions.css(self,'body > div:nth-child(32) > div > div.lisBox > div.List-Box > div > div:nth-child(14) > div.w6 > div:nth-child(1) > a').click()
#
#     def tearDown(self) -> None:
#         self.driver.quit()
# if __name__ == '__main__':
#     suite=unittest.TestSuite()
#     suite.addTest(Booking_tickes('test_ctrip_tickes'))
#     fileName='./test_ctrip_tickes.html'  #设置生成的报表html文件地址
#     fp=open(fileName,'wb')
#     # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test_Report_Portal',description='Report_Description')  #设置报表页面的title和报表总结描述内容
#     # runner.run(suite)
#     fp.close()
class Booking_tickes(unittest.TestCase):
    def test_ctrip_tickes(self):
        functions.log(self, 'Read Excel Files to get test data.')
        dic1 = functions.read_excel(self, 'station.xlsx', 0)
        print(self, dic1[1][0], dic1[1][1])

        functions.log(self, 'Begin to search tickes.')
        Search.search_ticks(self, dic1[0][0], dic1[0][1], 1)
        functions.log(self, 'End to search tickes.')
        functions.log(self, "Begin to get driver object")
        self.driver = functions.driver(self)

        time.sleep(2)  # 在页面跳转时加上时间等待，避免元素定位出现异常
        functions.log(self, 'Click book button:)')
        functions.css(self,'body > div:nth-child(32) > div > div.lisBox > div.List-Box > div > div:nth-child(14) > div.w6 > div:nth-child(1) > a').click()
book=Booking_tickes()
book.test_ctrip_tickes()