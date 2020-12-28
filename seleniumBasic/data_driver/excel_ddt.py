# -*- coding:utf-8 -*-
# @Time : 2020-12-03 13:58
# @Author: Danica
# @File : excel_ddt.py
# import xlrd
import pytest
# def get_data():
#     filename='excel.xlsx'
#     wb=xlrd.open_workbook(filename)
#     sheet=wb.sheet_by_index(0)
#     rows=sheet.nrows
#     cols=sheet.ncols
#     lst=[]
#     for row in range(rows):
#         for col in range(cols):
#             cell_data=sheet.cell_value(row,col)
#             lst.append(cell_data)
#     return lst
#
# @pytest.mark.parametrize('name',get_data())
# def test(name):
#     print(name)

if __name__ == '__main__':
    # print(get_data())
    pytest.main(['-sv', 'excel_ddt.py'])







