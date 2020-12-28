# -*- coding:utf-8 -*-
# @Time : 2020-10-27 16:14
# @Author: Danica
# @File : test1.py

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print(i, j, k)
