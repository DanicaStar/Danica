# -*- coding:utf-8 -*-
# @Time : 2020-11-01 16:35
# @Author: Danica
# @File : test7.py
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,j*i),end=' ')
    print()