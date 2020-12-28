# -*- coding:utf-8 -*-
# @Time : 2020-10-19 19:42
# @Author: Danica
# @File : case3.py


from interface.common.common import Common
#建立和WebSocket接口的链接
con=Common('ws://echo.websocket.org','ws')
# 获取返回结果
result = con.send('Hello, World...')
#打印日志
print(result)
#释放WebSocket的长连接
del con