# -*- coding:utf-8 -*-
# @Time : 2020-11-02 18:45
# @Author: Danica
# @File : test10.py
import time
print(time.time())     #时间戳
print(time.localtime(time.time()))    #time.struct_time(tm_year=2020, tm_mon=11, tm_mday=1, tm_hour=16, tm_min=44, tm_sec=7, tm_wday=6, tm_yday=306, tm_isdst=0)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))   #格式化时间格式  2020-11-01 16:44:07