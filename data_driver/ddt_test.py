# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 2:58 下午
# @Author  : danica
# @FileName: ddt_test.py
# @Software: PyCharm


import os
from ddt import ddt, data, unpack, file_data
import unittest


def get_data():
    test_data = [{'name': 'danica', 'age': 18}, {'name': 'Tom', 'age': 20}]
    return test_data


@ddt()
class TestDdt(unittest.TestCase):
    # # 读取元组数据-单组元素
    # @data(1,2,3)
    # def test1(self,value):
    #     print(value)
    #
    # # 读取元组数据-多组元素
    # @data((1, 2, 3),(4,5,6))
    # def test2(self,value):
    #     print(value)
    #
    # #读取元组数据-拆分
    # @data((1, 2, 3), (4, 5, 6))
    # @unpack
    # def test3(self, value1,value2,value3):
    #     print(value1,value2,value3)
    #
    # #读取列表
    # @data([{'name':'danica','age':18},{'name':'Tom','age':20}])
    # def test4(self, value):
    #     print(value)
    #
    #
    # # 字典
    # @data({'name': 'danica', 'age': 18}, {'name': 'Tom', 'age': 20})
    # def test5(self, value):
    #     print(value)

    # #字典-拆分
    # @data({'name':'danica','age':18},{'name':'Tom','age':20})
    # @unpack
    # def test6(self,name,age):
    #     print(name,age)

    # # 变量或者方法调用
    # test_data=[{'name':'danica','age':18},{'name':'Tom','age':20}]
    # # @data(*test_data)
    # @data(get_data())
    # def test7(self,value):
    #     print(value)

    # 读文件
    @file_data(os.getcwd() + '/data.json')
    def test8(self, value):
        print(value)


if __name__ == '__main__':
    unittest.main()
