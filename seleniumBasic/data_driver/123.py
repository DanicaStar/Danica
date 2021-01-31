# -*- coding:utf-8 -*-
# @Time : 2020-11-30 20:37
# @Author: Danica
# @File : 123.py





from seleniumBasic.data_driver.mysql import config,opmysql
import requests,logging
class Params_request():
    def __post(self,url,header,parama):
        try:
            if url !='':
                response=requests.post(url,header,parama)
                if response.status_code==200:
                    result={'code':'0000','message':'成功','data':response.text}
                else:
                    result = {'code': '2004', 'message': '状态吗不正确', 'data':[]}
            if url =='':
                result = {'code': '2002', 'message': '接口地址为空', 'data': []}
            else:
                result = {'code': '2003', 'message': '接口地址不正确', 'data': []}
        except Exception as error:
            result = {'code': '9999', 'message': '系统异常', 'data': []}
        return result

