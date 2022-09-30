# -*- coding: utf-8 -*-
# @Time    : 2022/9/22 5:32 下午
# @Author  : danica
# @FileName: xlrd_read.py
# @Software: PyCharm


import xlrd


class OperationExcel:
    def __init__(self, filename):
        self.table = xlrd.open_workbook(filename)
        """
        初始化类，每次传入文件名
        filename：文件路径+文件名
        """

    def get_data_by_index(self, index=0):
        sheet = self.table.sheet_by_index(index)
        return self._get_data_by_info(sheet)

    def get_data_by_name(self, name):
        sheet = self.table.sheet_by_index(name)
        return self._get_data_by_info(sheet)

    def _get_data_by_info(self, sheet):
        """
            将表格的数据读取成 [{},{},{}....]
            字典的键：表格的第一行
            字典的值：表格的其他行
            Excel数据类型   python数据类型
            1                str
            2                整数
            3                日期
            4                布尔值

        """
        key = sheet.row_values(0)
        rows = sheet.nrows
        cols = sheet.ncols
        data_list = []
        for row in range(1, rows):
            values = []
            for col in range(cols):
                value = self.read_cell(sheet, row, col)
                values.append(value)
            tmp = zip(key, values)
            data_list.append(dict(tmp))
            # values = sheet.row_values(row)
            # tmp = zip(key, values)
            # data_list.append(dict(tmp))
        return data_list

    # 处理单元格数据类型
    def read_cell(self, sheet, row, col):
        cell_value = sheet.cell_value(row, col)
        cell_type = sheet.cell_type(row, col)
        if cell_type == 1:
            cell_value = cell_value
        elif cell_type == 2 and cell_type // 1 == 0:
            cell_value = int(cell_value)
        elif cell_type == 4:
            cell_value = True if cell_value == 1 else False
        return cell_value


if __name__ == '__main__':
    test = OperationExcel('./data/login.xls')
    print(test.get_data_by_index())
