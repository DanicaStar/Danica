# -*- coding:utf-8 -*-
# @Time : 2021-02-19 19:58
# @Author: Danica
# @File : 8_shuixianhua.py
#水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）

# for i in range(100,1000):
#     sum=0
#     j=i
#     while j>10:
#         x=j%10   #个位数
#         j=j//10  #每次除10后的正数部分
#         sum+=x**3
#     else:
#         sum+=j**3
#     if i==sum:
#         print(i)


list1=[20, 70, 110, 150]
for i in range( len(list1)):
    for j in range(i,len(list1)):
        if list1[i]+list1[j]==90:
            print(i,j)