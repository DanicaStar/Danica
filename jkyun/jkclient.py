# -*- coding: utf-8 -*-
import hashlib
import json
import time
import requests
import threading
reqcommon = {
    'appkey': 'app_jackyun_manager',
    'secret': 'app_jackyun_manager_secret'
}

class jkClient:
    '模拟吉客云客户端'
    # 登录信息记录（含token）
    __loginCache = {}
    # 全局缓存
    cacheData = {}
    # 登录状态
    hasLogin = False

    def __print_log(self, log):
            print('{} {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), log))

    def __md5(self, s):
        hl = hashlib.md5()   
        hl.update(s.encode(encoding='utf-8'))
        return hl.hexdigest().upper()      

    def __getSign(self, params):
        sorted_keylist = sorted(params)
        sign = ''
        for key in sorted_keylist:
            sign = '{}{}{}'.format(sign, key, params[key])
        sign = '{}{}{}'.format(reqcommon['secret'], sign, reqcommon['secret'])
        return self.__md5(sign)

    def __dataPackage(self, data):
        data['appkey'] = reqcommon['appkey']
        data['access_token'] = 'Bearer {}'.format(self.__loginCache.get('access_token'))
        data['timestamp'] = (int(round(time.time() * 1000)))
        sign = self.__getSign(data)
        data['sign'] = sign
        
        return data    

    def httpPost(self, url, data = None, headers = None):
        if url is None:
            return
        # 若url不全，自动补齐网关部分
        if url.find('http://') < 0:
            url = ''.join([self.cacheData['gateway'], url])
        if data is not None:
            data = self.__dataPackage(data)
        ssrequest = requests.session()
        ssrequest.headers = headers
        try:
            rsp = ssrequest.post(url, data = data)
        except Exception:
            return '接口调用异常'

        return rsp.text

    def httpGet(self, url, data = None, headers = None):
        """
        get请求吉客云接口
        Args:
            url: 接口地址，可忽略网关地址
            data: 请求参数，可为空，不为空时自动拼接到url后方（不要传与业务无关的公共参数）
            headers: 带header请求，一般不传
        Returns:
            返回requests.Response.text
            example:
                {'}
        """
        if url == None:
            return
        # 若url不全，自动补齐网关部分
        if url.find('http://') < 0:
            url = ''.join([self.cacheData['gateway'], url])
        if data == None: data = {}

        data = self.__dataPackage(data)
        params = ''
        for key in data:
            params = '{}{}={}&'.format(params, key, data[key])
        url = '{}{}{}'.format(url, '&' if url.find('?') > 0 else '?', params)
        
        ssrequest = requests.session()
        ssrequest.headers = headers
        try:
            rsp = ssrequest.get(url, data = data)
        except Exception:
            return '接口调用异常'
            
        return rsp.text

    def __init__(self, gateway):
        self.cacheData['gateway'] = gateway

    def loginV1(self, memberName, authCode, userName, password):
        self.__print_log('正在以会员{} 账号{}身份登录'.format(memberName, userName))

        url = '{}/auth/login'.format(self.cacheData['gateway'])
        data = {}
        #data['grant_type'] = 'password'
        data['username'] = userName
        data['membername'] = memberName    
        data['ati'] = '17025E0928007A20832D484D7EB4ACB0'
        #data['appkey'] = reqcommon['appkey']
        data['timestamp'] = (int(round(time.time() * 1000)))
        data['membercode'] = self.__md5('{}{}'.format(authCode, data['timestamp']))
        data['password'] = self.__md5('{}{}'.format(self.__md5('{}{}'.format(userName, password)), data['timestamp']))

        # 参数拼接
        params = ''
        for key in data:
            params = '{}{}={}&'.format(params, key, data[key])
        url = '{}?{}'.format(url, params)
        
        # Authorization信息写死
        headers = {}
        # headers['Authorization'] = 'Basic YXBwX2phY2t5dW5fbWFuYWdlcjphcHBfamFja3l1bl9tYW5hZ2VyX3NlY3JldA=='
        headers['clientId'] = 'app_jackyun_manager'
        # 获取token
        rspLogin = self.httpPost(url, None, headers)
        loginJson = json.loads(rspLogin)
        if loginJson.get('error') != None:
            self.__print_log('登录失败：{}'.format(loginJson.get('error_description')))
            return
        
        # 记录登录信息
        self.__loginCache = loginJson
        memberHolder = {}
        self.cacheData['memberHolder'] = memberHolder
        memberHolder['memberName'] = self.__loginCache.get('member_name') 
        memberHolder['userName'] = self.__loginCache.get('user_name') 
        memberHolder['groupId'] = self.__loginCache.get('group_id') 

        # 定期刷新token
        self.__autoRefreshToken()

        self.__print_log('登录成功')

    def login(self, memberName, authCode, userName, password):
        self.hasLogin = False
        self.__print_log('正在以会员{} 账号{}身份登录'.format(memberName, userName))

        url = '{}/auth/getUserId?memberName={}&userName={}'.format(self.cacheData['gateway'], memberName, userName)
        rspGetUserId = requests.get(url).text
        rspJson = json.loads(rspGetUserId)
        if rspJson.get('code') != 200:
            self.__print_log('登录失败：{}'.format(rspJson.get('msg')))
            return False

        userId = rspJson.get('result').get('data')

        url = '{}/auth/v2/login'.format(self.cacheData['gateway'])
        data = {}
        #data['grant_type'] = 'password'
        data['userId'] = userId
        data['memberName'] = memberName    
        data['ati'] = '17025E0928007A20832D484D7EB4ACB0'
        data['timestamp'] = (int(round(time.time() * 1000)))
        data['password'] = self.__md5('{}{}'.format(self.__md5('{}{}'.format(userId, password)), data['timestamp']))

        # 参数拼接
        params = ''
        for key in data:
            params = '{}{}={}&'.format(params, key, data[key])
        url = '{}?{}'.format(url, params)
        
        # Authorization信息写死
        headers = {}
        # headers['Authorization'] = 'Basic YXBwX2phY2t5dW5fbWFuYWdlcjphcHBfamFja3l1bl9tYW5hZ2VyX3NlY3JldA=='
        headers['clientId'] = 'app_jackyun_manager'
        # 获取token
        rspLogin = self.httpPost(url, None, headers)
        loginJson = json.loads(rspLogin)
        if loginJson.get('error') != None:
            self.__print_log('登录失败：{}'.format(loginJson.get('error_description')))
            return False
        
        # 记录登录信息
        self.__loginCache = loginJson
        memberHolder = {}
        self.cacheData['memberHolder'] = memberHolder
        memberHolder['memberName'] = self.__loginCache.get('member_name') 
        memberHolder['userName'] = self.__loginCache.get('user_name') 
        memberHolder['groupId'] = self.__loginCache.get('group_id') 

        # 定期刷新token
        self.__autoRefreshToken()

        self.__print_log('登录成功')

        self.hasLogin = True
        return True

    def __refreshToken(self):
        if self.__loginCache == {}:
            return

        self.__print_log('开始自动刷新token')
        url = '{}/auth/refresh'.format(self.cacheData['gateway'])
        data = {}
        #data['granttype'] = 'refreshtoken'
        data['refreshToken'] = self.__loginCache.get('refresh_token')

        # 参数拼接
        params = ''
        for key in data:
            params = '{}{}={}&'.format(params, key, data[key])
        url = '{}?{}'.format(url, params)

        # Authorization信息写死
        headers = {}
        # headers['Authorization'] = 'Basic YXBwX2phY2t5dW5fbWFuYWdlcjphcHBfamFja3l1bl9tYW5hZ2VyX3NlY3JldA=='
        headers['clientId'] = 'app_jackyun_manager'
        # headers['memberName'] = self.__loginCache.get('member_name') 

        # 刷新token
        rspLogin = self.httpPost(url, None, headers)
        loginJson = json.loads(rspLogin)
        if loginJson.get('error') != None:
            self.__print_log('刷新授权失败：{}'.format(loginJson.get('error_description')))
            return
        
        # 记录登录信息
        self.__loginCache = loginJson
        # 定期刷新token
        self.__autoRefreshToken()

        self.__print_log('刷新授权成功')
    
    def __autoRefreshToken(self):
        if self.__loginCache == {}:
            return

        # 每小时刷新一次
        refreshTimer = threading.Timer(1800, self.__refreshToken)
        refreshTimer.start()
