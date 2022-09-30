# -*- coding:utf-8 -*-
# @Time : 2020-12-12 21:12
# @Author: Danica
# @File : 3_bounder.py
import re

# 1、"^" 匹配字符串开头

# 2、"$"匹配字符串结尾
#result=re.match(r'1[35678]\d{9}$','13345678901')   #限制了只能11位

# 3、"\b"匹配一个单词的边界
result=re.match(r'.+\bll\b','he ll o')   #匹配的字符串单词左右边不为空则范围None

print(result)

# 4、"\B"匹配单词非边界
# result=re.match(r'.+ll\B','hello')     #匹配的字符串单词右边为空则范围None