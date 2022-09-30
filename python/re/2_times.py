# -*- coding:utf-8 -*-
# @Time : 2020-12-12 21:12
# @Author: Danica
# @File : 2_times.py
import  re

# 1、"*"  匹配前一个字符出现0/无数次，可有可无
# result=re.match('\d*','1a23abc')

# 2、"+"  匹配前一个字符出现1/无数次，至少一次
# result=re.match('\d+','a23abc')

# 3、"？" 匹配前一个字符出现1/0次，要么一次，要么没有
# 3result=re.match('\d?\w','4123a23abc')

# 4、{m}  匹配前一个字符出现m次
# result=re.match('\d{2}\w','4123a23abc')


# 5、{m,} 匹配前一个字符至少出现m次
# result=re.match('\d{2,}\w','4123a23abc')

# 6、{m,n}匹配前一个字符出现从m到n次
# result=re.match('\d{2,3}\w','12345a2345')


#手机号规则
# result=re.match('1[35678]\d{9}','13345678901123')    #没有限制11位
#result=re.match(r'1[35678]\d{9}$','13345678901')   #限制了只能11位


# 转义字符匹配
# s='\\nabc'
# result=re.match('\\\\n\w',s)
# result=re.match(r'\\n\w',s)




