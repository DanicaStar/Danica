# -*- coding:utf-8 -*-
# @Time : 2021-03-02 20:53
# @Author: Danica
# @File : exercise2.py
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#count=0
#for i in range(1,5):
#    for j in range(5):
#        for k in range(5):
#            if i!=j and j!=k and i!=k:
#                print(i,k,j)
#                count+=1
#print(count)

#2、
'''
企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
lirun=[100,60,40,20,10,0]
rate=[0.01,0.015,0.03,0.05,0.075,0.1]
money=input('请输入应发放的奖金总额：')
def get_salary(money):
    for i in lirun:
        if int(money)>i:
            salary_end= (int(money)-i)*rate[i]
    return salary_end

get_salary(money)
