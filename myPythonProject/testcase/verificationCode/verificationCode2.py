# -*- coding:utf-8 -*-
# @Time : 2020-12-03 19:45
# @Author: Danica
# @File : verificationCode2.py
# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
#第三方api识别验证码
from myPythonProject.lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","377219","5ccd886ca0db45e28b352d8177d74cab" )
r.addFilePara("image", "test.png")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
result=res.text
body = res.json()['showapi_res_body']    #字符串要转换为字典格式
code = body['Result']
print(result)
print(code)