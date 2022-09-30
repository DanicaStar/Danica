# -*- coding: utf-8 -*-
import os
import json
import time
import hashlib
import logging
import threading
import datetime
import sys
from jkyun.jkclient import jkClient
logPath = os.path.join(os.path.dirname(__file__) + '/', '233668_query.log')
logging.basicConfig(filename=logPath, format='%(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 登录
MODE = 'test'
MAX_COUNT = 300000
jkConfMaps = {
    'dev': {'url': 'http://192.168.88.51', 'memberName': 'jackyun_dev', 'authCode': 'ABCDEFG', 'userName': 'zb', 'password': 'zb1234'},
    'test': {'url': 'http://192.168.88.186:31088', 'memberName': '420001', 'authCode': 'ABCDEFG', 'userName': '18167200070', 'password': 'cy902518'}
}
jkConf = jkConfMaps[MODE]

def login_jkyun():
    jkClient.login(jkConf['memberName'], jkConf['authCode'],
                   jkConf['userName'], jkConf['password'])


jkClient = jkClient(jkConf['url'])
login_jkyun()

def order_create():

    createBillJson = {
        "billType":"21","billSource":2,"companyName":"卡布奇洛测试公司","companyFcCode":"CNY","companyFcName":"人民币","bpClass":"15","billNum":"","companyId":"711474021267505792","billDate":"2020-06-13","tranCode":"YR0100004","tranName":"狼堡-应收小羊","recPay":4,"fcCode":"CNY","fcName":"人民币","fcRate":1,"oriBillNum":"","vendId":"912177732229891328","vendName":"wms供应商3","endDate":"2020-06-13","textLine":"应收单","tranAmountSum":"120.00","receTranAmount":"120.00","baseAmountSum":"120.00","receBaseAmount":"120.00","billTransDetailCreateDtoList":[{"recPay":4,"bpClass":"15","itemCode":"YR0100004","vendId":"912177732229891328","billDate":"2020-06-13","endDate":"2020-06-13","oriBillNum":"","fcCode":"CNY","fcRate":1,"textLine":"应收单","vendName":"wms供应商3","tranCode":"YR0100004","tranName":"狼堡-应收小羊","fcName":"人民币","jd":"1","isVerification":1,"accountType":2,"trValue":"120.00","cuValue":"120.00"},{"recPay":1,"bpClass":"15","itemCode":"ZC1000","billDate":"2020-06-13","endDate":"2020-06-13","oriBillNum":"","fcCode":"CNY","fcRate":1,"receTranAmount":"120.00","receBaseAmount":"120.00","textLine":"应收单","tranCode":"YR0100004","tranName":"狼堡-应收小羊","fcName":"人民币","jd":"2","isVerification":0,"accountType":3,"trTax":"0.00","cuTax":"0.00","taxRate":0,"_id":35,"_uid":35,"_state":"added","deptType":"4","deptId":"753516591724528000","deptName":"生产","itemName":"水电费","taxRateText":0,"trTaxValue":"120.00","trValue":"120.00","cuTaxValue":"120.00","cuValue":"120.00","orderBy":1}]
    }

    data = {'createBillJson': json.dumps(createBillJson)}
    rsp = jkClient.httpPost("/jkyun/fin-fbs/billtranscreate/createbill", data)
    rspjson = json.loads(rsp)

    if rspjson.get("code") != 200:
        login_jkyun()
        order_create()
    else:
        print(rsp)


def main():
    pass


if __name__ == '__main__':

    orderCount = 0
    while orderCount < MAX_COUNT:
        order_create()
        print('已创建' + str(orderCount) + '条数据')
        orderCount += 1
    pass
    print("创建完成")