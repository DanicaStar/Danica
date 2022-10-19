# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 7:13 下午
# @Author  : danica
# @FileName: decorator2.py
# @Software: PyCharm

# 装饰器无参数，被装饰函数有参数
"""
需求：利用装饰器，来计算fun1函数的运行时间
"""
import time


def outer(origin):
    def inner(*args, **kwargs):
        time1 = time.time()
        res = origin(*args, **kwargs)
        time2 = time.time()
        times = round((time2 - time1) * 1000, 6)
        return res, times

    return inner


@outer
def fun1(num):
    return num


@outer
def fun2(num1, num2):
    return num1, num2


num1 = [1, 2, 3]
num2 = [2, 3, 4]
print(fun1(num1))
print(fun2(num1, num2=num2))
