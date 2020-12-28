# -*- coding:utf-8 -*-
# @Time : 2020-11-14 16:53
# @Author: Danica
# @File : test_08.py
import pytest
import allure
@pytest.fixture(scope='session')
def login():
    print('用例先登录')

@allure.step('步骤1：点XXX')
def step_1():
    print('111')

@allure.step('步骤2：点XXX')
def step_2():
    print('222')

@allure.feature('编辑页面')
class TestEditPage():
    '''编辑页面'''

    @allure.story('这是一个XXX的用例')
    def test_1(selfself,login):
        '''用例描述：先登录，再去执行XXX'''
        step_1()
        step_2()
        print("XXX")

    @allure.story('打开a页面')
    def test_2(selfself,login):
        '''用例描述：先登录，再去执行yyy'''
        print("yyy")

if __name__ == '__main__':
    #注意生成测试报告，必须在命令行执行
    #pytest --alluredir  ./report test_08.py
    #allure serve ./report  启动allure查看报告
    pytest.main(['--alluredir','./reports','test_08.py'])