# -*- coding: utf-8 -*-
# @Time    : 2022/10/19 7:13 下午
# @Author  : danica
# @FileName: decorator3.py
# @Software: PyCharm

# 装饰器有参数，被装饰函数有参数
"""
需求：利用装饰器，来计算fun1函数的运行时间
"""
import time


def wrapper_out(params):
    def outer(origin):
        def inner(*args, **kwargs):
            time1 = time.time()
            res = origin(*args, **kwargs)
            time2 = time.time()
            times = round((time2 - time1) * 1000, 6)
            return res, times, params

        return inner

    return outer


params = [11, 22, 33]


@wrapper_out(params)
def fun1(num):
    return num


@wrapper_out(params)
def fun2(num1, num2):
    return num1, num2


# num1 = [1, 2, 3]
# num2 = [2, 3, 4]
# print(fun1(num1))
# print(fun2(num1, num2=num2))


#  多个装饰器
def demo1(func):
    print('1' * 10)
    def one():
        print('2' * 10)
        func()
        print('3' * 10)
    return one


def demo2(func):
    print('a' * 10)
    def two():
        print('b' * 10)
        func()
        print('c' * 10)
    return two


@demo1
@demo2
def test():
    print('test test')


test()
