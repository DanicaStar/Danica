# -*- coding:utf-8 -*-
# @Time : 2020-12-12 21:10
# @Author: Danica
# @File : 1_tongpeifu.py
import  re
# 1、" . "匹配任意一个字符（除了\n）
# result=re.match('.','abc')
# result=re.match('.','\n')

# 2、"\d"匹配数字，即0-9 ==》[0-9]
# result=re.match('\d','123')

# 3、"\D"匹配非数字   ==》[^0-9]
# result=re.match('\D','a123')


# 4、"\s"匹配空白，即空格/tab键  \t \r \n
# result=re.match('\s','\ra')

# 5、"\S"匹配非空白
# result=re.match('\S','a')

# 6、"\w"匹配单词字符，即a-z,A-Z,0-9  ==》[a-zA-Z0-9_]
result=re.match('\w','_a')

# 7、"\W"匹配非字符  ==》[^a-zA-Z0-9_]
# 8、"[]"匹配[]中列举的字符,[^]列举字符取反
result=re.match('1[a-z5-9]','19')   #表示第一位是1，第二位a-z，或5-9



print(result.group())