# -*- coding:utf-8 -*-
# @Time : 2020-10-28 18:52
# @Author: Danica
# @File : test4.py
#题目：输入某年某月某日，判断这一天是这一年的第几天？

year=int(input("请输入year：\n"))
month=int(input("请输入month:\n"))
day=int(input("请输入day:\n"))

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 1<=month<=12:
    sum=months[month-1]
    sum+=day
else:
    print("日期输入错误")
if year%400==0 or year%4==0 and year%100!=0:
    leap=1
if leap==1 and month>2:
    sum+=1

print('it is the %dth day.' % sum)