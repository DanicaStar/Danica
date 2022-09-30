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
MAX_COUNT = 5
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
        "unitId":"911452646145163904","unitName":"木易","custId":"911452646145163904","custName":"木易","billNum":"","billType":"22","billSource":2,"companyId":"711474021267505792","companyName":"卡布奇洛测试公司","companyFcCode":"CNY","companyFcName":"人民币","billDate":"2020-06-13","tranCode":"YR0100003","tranName":"羊村-应付小羊","recPay":3,"fcCode":"CNY","fcName":"人民币","fcRate":1,"oriBillNum":"","bpClass":"客户档案","endDate":"2020-06-13","textLine":"应付单","tranAmountSum":"110.00","receTranAmount":"110.00","baseAmountSum":"110.00","receBaseAmount":"110.00","billTransDetailCreateDtoList":[{"recPay":3,"bpClass":"客户档案","itemCode":"YR0100003","custId":"911452646145163904","billDate":"2020-06-13","endDate":"2020-06-13","oriBillNum":"","fcCode":"CNY","fcRate":1,"textLine":"应付单","custName":"木易","tranCode":"YR0100003","tranName":"羊村-应付小羊","fcName":"人民币","jd":"2","isVerification":1,"accountType":2,"trValue":"110.00","cuValue":"110.00"},{"recPay":1,"bpClass":"客户档案","itemCode":"ZC004","billDate":"2020-06-13","endDate":"2020-06-13","oriBillNum":"","fcCode":"CNY","fcRate":1,"receTranAmount":"110.00","receBaseAmount":"110.00","textLine":"应付单","tranCode":"YR0100003","tranName":"羊村-应付小羊","fcName":"人民币","jd":"1","isVerification":0,"accountType":3,"trTax":"0.00","cuTax":"0.00","taxRate":0,"_id":8,"_uid":8,"_state":"added","deptType":"3","deptId":"711474388453655168","deptName":"研发","itemName":"补偿退款支出","taxRateText":0,"trTaxValue":"110.00","trValue":"110.00","cuTaxValue":"110.00","cuValue":"110.00","orderBy":1}]   
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