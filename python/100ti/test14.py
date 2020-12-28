# -*- coding:utf-8 -*-
# @Time : 2020-11-12 21:23
# @Author: Danica
# @File : test14.py
#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
from math import sqrt
def func(n):
    print('%d=' % n,end='')
    while 1:
        for i in range(2,int(sqrt(n))+1):
            if n % i ==0:
                print('%d*' % i,end='')
                n=int(n/i)
                break
        else:
            print(n)
            break
num=int(input("请输入一个数："))
func(num)




