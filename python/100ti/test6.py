# -*- coding:utf-8 -*-
# @Time : 2020-11-01 16:10
# @Author: Danica
# @File : test6.py

def func(num):
    for x in range(num):
        if num==1 or num==2:
            return 1
        else:
            return func(num-1)+func(num-2)
            print(func(num-1)+func(num-2))

num=int(input("请输入数字："))
print(func(num))
