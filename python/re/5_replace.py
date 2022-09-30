# -*- coding:utf-8 -*-
# @Time : 2020-12-12 21:13
# @Author: Danica
# @File : 5_replace.py
import re
'''
s='<html><h1>小丸子</h1></html>'
result=re.search(r'小丸子',s)   #从左开始寻找，找到第一个符合的就匹配，后面就不再匹配
result=re.search(r'^小丸子$',s)  #必须以小丸子开头和结尾
print(result.group())
'''

# 替换
# result=re.sub(r'php','java','python c++ c ')
result='python=1000,c++=10,c=90'
def replace(result):
    r=int(result.group())+50
    return str(r)
result1=re.sub(r'\d+',replace,result)
print(result1)