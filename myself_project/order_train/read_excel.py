# -*- coding:utf-8 -*-
# @Time : 2021-01-13 20:05
# @Author: Danica
# @File : read_excel.py

import xlrd

wb=xlrd.open_workbook('pom/station.xlsx')
sheet=wb.sheet_by_index(0)
rows=sheet.nrows
cols=sheet.ncols
dic={}
for i in range(rows):
    data=[]
    for j in range(cols):
        data.append(sheet.col_values(j)[i])
        dic[i]=data
print(dic)
