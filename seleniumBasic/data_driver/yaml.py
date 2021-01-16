# -*- coding:utf-8 -*-
# @Time : 2021-01-13 19:47
# @Author: Danica
# @File : yaml.py

import yaml
file_2=open('yaml.yml')
yml=yaml.load(file_2,Loader=yaml.FullLoader)
print(yml)
print(type(yml))

# file_3=open('yaml.yml')
# yml_3=yaml.load_all(file_3,Loader=yaml.FullLoader)
# print(yml_3)
# print(type(yml_3))
