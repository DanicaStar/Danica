# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 5:34 下午
# @Author  : danica
# @FileName: xlwt_write.py
# @Software: PyCharm

import xlwt

# 新建文件
wk = xlwt.Workbook()
# 新建表sheet
sheet = wk.add_sheet('Danica')
# 写入数据，前两个参数，表示表的坐标，（0，0）表示第一个单元格
sheet.write(1, 1, "3")
# 保存文件
wk.save("./data/test123.xls")
