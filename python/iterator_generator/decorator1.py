# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 6:30 下午
# @Author  : danica
# @FileName: decorator1.py
# @Software: PyCharm

# 装饰器、装饰函数都无参数
"""
需求：利用装饰器，来计算fun1函数的运行时间
"""
import time


def outer(origin):
    def inner():
        time1 = time.time()
        res = origin()
        time2 = time.time()
        times = round((time2 - time1)*1000, 6)
        return res, times

    return inner


@outer
def fun1():
    value = [1, 2, 3]
    return value


print(fun1())
