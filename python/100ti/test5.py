# -*- coding:utf-8 -*-
# @Time : 2020-10-29 16:45
# @Author: Danica
# @File : test5.py
#输入三个整数x,y,z，请把这三个数由小到大输出
l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)