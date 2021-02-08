# -*- coding:utf-8 -*-
# @Time : 2021-02-04 18:28
# @Author: Danica
# @File : analyse.py
import openpyxl
from xlutils.copy import copy
import os,logging,datetime
from seleniumBasic.data_driver.mysql import config,opmysql
operation_db=opmysql.OperationDbInterface(link_type=1)  #实例化自动化测试数据库操作类
class AnalyseData():
    '''
    定义对接口测试数据进行分析的类
    1、导出数据到Excel中
    '''
    def  __init__(self):
        self.field=config.field_excle  #初始化配置文件

    def exportExcle(self,names_export):
        pass

if __name__ == '__main__':
    names_export=operation_db.select_one('select value_config from config_total where status=1 and key_config="name_export"')  #获取导出的接口数据元祖
    if names_export['code']=='0000':
        temp_export=eval(names_export['data'][0])  #获取查询数据，并将其转换成字典
        test_analyse_data=AnalyseData()
        result_export=test_analyse_data.exportExcle(temp_export) #导出结果
        print(result_export)
    else:
        print('获取导出的接口集失败')

