# -*- coding:utf-8 -*-
# @Time : 2021-01-24 11:52
# @Author: Danica
# @File : 123.py

import logging
class Test():
    def __init__(self,num):
        self.num=num

    def unnormal(self):
        try:
            print('开始测试异常情况')
            r=10/self.num
            print('result',r)

        except TypeError as e:
            print('TypeError', e)
        except ZeroDivisionError as e:
            print(logging.exception(e))
        finally:
            print('finally finish!')

test=Test(0)
test.unnormal()


create table