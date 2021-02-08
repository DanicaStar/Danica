# -*- coding:utf-8 -*-
# @Time : 2021-01-27 18:43
# @Author: Danica
# @File : compare.py
'''
定义数据比较方法
1、compare_param 是对外的参数比较类
2、compare_code 是关键参数值的比较方法
compare_params_complete 是参数完整性的比较方法
3、get_compare_params 是活的返回包数据去重后集合的方法
4、recure_params 递归操作方法，辅助去重
'''

import json, logging
from seleniumBasic.data_driver.mysql import config, opmysql

operation_db= opmysql.OperationDbInterface()   #s实例化测试数据库操作类
class CompareParam():
    #初始化数据
    def __init__(self,params_interface):
        self.params_interface=params_interface  #接口入参
        self.id_case=params_interface['id']
        self.result_list_response=[]
        self.params_to_compare=params_interface['params_to_compare']

    #定义关键参数值（code）比较
    def compare_code(self,result_interface):
        '''
        :param result_interface: HTTP返回包数据
        :return: 返回码code 返回信息message，数据data
        '''
        try:
            if result_interface.startswith('{') and isinstance(result_interface,str):
                temp_result_interface=json.loads(result_interface)   #将字符串类型转换成字典
                temp_code_to_compare=self.params_interface['code_to_compare']   #获取待比较code的名称
                if temp_code_to_compare in temp_result_interface.keys():
                    if str(temp_result_interface[temp_code_to_compare])==str(self.params_interface['code_expect']):
                        result={'code':'0000','message':'关键字参数值相同','data':[]}
                        operation_db.op_sql("Update case_interface set code_actual='%s',result_code_compare=%s where id=%s"%(temp_result_interface[temp_code_to_compare],1,self.id_case))
                    elif str(temp_result_interface[temp_code_to_compare])!=str(self.params_interface['code_expect']):
                        result = {'code': '1003', 'message': '关键字参数值不同', 'data': []}
                        operation_db.op_sql("Update case_interface set code_actual='%s',result_code_compare=%s where id=%s" % (temp_result_interface[temp_code_to_compare], 0, self.id_case))
                    else:
                        result = {'code': '1002', 'message': '关键字参数值比较出错', 'data': []}
                        operation_db.op_sql("Update case_interface set code_actual='%s',result_code_compare=%s where id=%s" % (temp_result_interface[temp_code_to_compare], 3, self.id_case))
                else:
                    result = {'code': '1001', 'message': '返回包数据无关键字参数', 'data': []}
                    operation_db.op_sql("Update case_interface set result_code_compare=%s, where id=%s" % ( 2, self.id_case))
            else:
                result = {'code': '1000', 'message': '返回包格式不合法', 'data': []}
                operation_db.op_sql("Update case_interface set result_code_compare=%s where id=%s" % (4, self.id_case))

        except Exception as error:
            result = {'code': '9999', 'message': '关键字参数值比较异常', 'data': []}
            operation_db.op_sql("Update case_interface set result_code_compare=%s' where id=%s" % (9, self.id_case))
            logging.basicConfig(
                filename=config.src_path+'/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger=logging.getLogger(__name__)
            logger.exception(error)
        finally:
            return result



    #定义将接口返回数据中的参数名写入到列表中
    def get_compare_params(self,result_interface):
        '''
        :param result_interface: HTTP返回报数据
        :return: 返回码code，返回信息message，数据data
        '''
        try:
            if result_interface.startswith('{') and isinstance(result_interface,str):
                temp_result_interface=json.load(result_interface)
                self.result_list_response=temp_result_interface.keys()
                result = {'code': '0000', 'message': '成功', 'data': self.result_list_response}
            else:
                result = {'code': '1000', 'message': '返回包格式不合法', 'data':[]}
        except Exception as error:
            result = {'code': '9999', 'message': '处理参数异常', 'data': []}
            logging.basicConfig(
                filename=config.src_path+'/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger=logging.getLogger(__name__)
            logger.exception(error)
        finally:
            return result

    #参数完整性比较方法，比较传参值与 __recur_params方法返回的结果
    def compare_params_complete(self,result_interface):
        try:
            temp_compare_params=self.__recur_params(result_interface)   #获取返回包的参数集
            if temp_compare_params['code']=='0000':
                temp_result_response=temp_compare_params['data']   #获取接口返回参数去充列表
                if self.params_to_compare.startswith('[') and isinstance(self.params_to_compare,str):   #判断测试用例表中预期结果集是否为列表
                    list_params_to_compare=eval(self.params_to_compare)  #将数据库表中的Unicode编码数据转换成原列表
                    if set(list_params_to_compare).issubset(set(temp_result_response)):  #判断集合的包含关系
                        result={'code': '0000', 'message': '参数完整性比较一致', 'data': []}
                        operation_db.op_sql("Update case_interface set params_actual='%s',result_params_compare=%s where id=%s" % (temp_result_response, 1, self.id_case))
                    else:
                        result = {'code': '3001', 'message': '实际结果中元素不都在预期结果中', 'data': []}
                        operation_db.op_sql("Update case_interface set params_actual='%s',result_params_compare=%s where id=%s" % (temp_result_response, 0, self.id_case))
                else:
                    result = {'code': '4001', 'message': '用例中待比较参数集错误', 'data':self.params_to_compare}
            else:
                result = {'code': '2001', 'message': '调用__recur_params方法返回错误', 'data': []}
                operation_db.op_sql("Update case_interface set result_params_compare=%s where id=%s" % (2, self.id_case))
        except Exception as error:
            return {'code': '9999', 'message': '参数完整性比较异常', 'data': []}
            operation_db.op_sql("Update case_interface set result_params_compare=%s where id=%s" % (9, self.id_case))
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(error)
        finally:
            return result



    #定义递归方法
    def __recur_params(self,result_interface):
        #定义递归操作。将接口返回数据中的参数名写入到列表中（去重）
        try:
            if result_interface.startswith('{') and isinstance(result_interface,str):
                temp_result_interface=json.load(result_interface)
                self.__recur_params(temp_result_interface)
            elif isinstance(result_interface,dict):
                for param,value in result_interface.items():
                    self.result_list_response.append(param)
                    if isinstance(value,list):
                        for param in value:
                            self.__recur_params(param)
                    elif isinstance(value,dict):
                        self.__recur_params(value)
                    else:
                        continue
            else:
                pass
        except Exception as error:
            logging.basicConfig(
                filename=config.src_path + '/log/syserror.log',
                level=logging.DEBUG,
                format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s'
            )
            logger = logging.getLogger(__name__)
            logger.exception(error)
            return {'code': '9999', 'message': '处理数据异常', 'data': []}
        return {'code': '0000', 'message': '成功', 'data': list(set(self.result_list_response))}


if __name__ == '__main__':
    sen_sql='select * from case_interface where name_interface="getIpinfo.php" and id=1'
    params_interface=operation_db.select_one(sen_sql)
    data=params_interface['data'][0]
    result_interface=data['result_interface']
    test_compare_param=CompareParam(params_interface['data'])
    result_compare_code=test_compare_param.compare_code(result_interface)  #关键参数值比较
    print(result_compare_code)
    result_compare_params_complete=test_compare_param.compare_params_complete(result_interface)  #参数完整性比较
    print(result_compare_params_complete)


