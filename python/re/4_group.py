# -*- coding:utf-8 -*-
# @Time : 2020-12-12 21:13
# @Author: Danica
# @File : 4_group.py
import re

# 1、"｜"  匹配左右任意一个表达式
# 匹配出0-100之间的数字
# result=re.match(r'[1-9]/d?|100$','0')
# result=re.match(r'[1-9]?/d?|0|100$','0')
'''
s='<h1>小丸子的哆啦A梦</h1>'
result=re.match(r'(<h1>).*(</h1>)',s)
print(result.group())    #<h1>小丸子的哆啦A梦</h1>
print(result.group(0))   #<h1>小丸子的哆啦A梦</h1>
print(result.group(1))   #<h1>
print(result.group(2))   #</h1>
print(result.groups())   #('<h1>', '</h1>')
'''



# 2、"(ab)"将括号中字符作为一个分组
# 3、"\num"引用分组num匹配到的字符串
'''
s='<html><h1>小丸子</h1></html>'
result=re.match(r'<(.+)><(.+)>.+</\2></\1>',s)   #2指的是第2个()中的值，1指的是第1个()中的值
print(result.group())
'''

# 4、"(?p<name>)" 分组起别名
# 5、"(?P<name>)" 引用别名为name分组匹配到的字符串

'''
s1='<html><h1>小丸子</h1></html>'
result1=re.match(r'<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>',s1)
print(result1.group())
'''

mail=r'\w+@(163|126|gmail|qq)\.(com|cn|net)$'