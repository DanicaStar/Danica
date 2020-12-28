# -*- coding:utf-8 -*-
# @Time : 2020-11-14 15:38
# @Author: Danica
# @File : test_05.py
'''
在pytest中，使用参数化测试：每组参数都独立运行一次
pytest.mark.parametrize(argnames,argvalues)
'''

'''
1、admain  123
2、admain  XXX
3、XXX  123
4、XXX  XXX
'''


import pytest
data1=['123','456']

@pytest.mark.parametrize('pwd',data1)
def test1(pwd):
    print(pwd)

#元组
data2=[
    (1,2,3),  #或者[1,2,3]
    (4,5,6)   #或者[4,5,6]
]
@pytest.mark.parametrize('a,b,c',data2)
def test1(a,b,c):
    print(a,b,c)

#字典
data3=(
    {
        'user':1,
        'pwd':'a'
    },
    {
        'age':3,
        'email':'danica@qq.com'
    }
)
@pytest.mark.parametrize('dic',data3)
def test1(dic):
    print(dic)

data_1=[
    pytest.param(1,2,3,id='(a+b):pass'), #id的值可以自定义，方便理解每个用例测试什么
    pytest.param(4,5,10,id='(a+b):fail'),
]
def add(a,b):
    return a+b

class TestParametrize():
    @pytest.mark.parametrize('a,b,expect',data_1)
    def test_parametrize_1(self,a,b,expect):
        assert add(a,b)==expect

if __name__ == '__main__':
    pytest.main(['-sv','test_05.py'])