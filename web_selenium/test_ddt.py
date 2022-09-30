# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 2:53 下午
# @Author  : danica
# @FileName: test_ddt.py
# @Software: PyCharm


from selenium import webdriver
from selenium.webdriver.common.by import By
from web_selenium.common.excel_util import ExcelUtil

import pytest


class TestCase:

    def setup(self):
        print('登陆浏览器')

    def teardown(self):
        print('关闭浏览器')

    @pytest.mark.parametrize('input_data', ExcelUtil().read_excel())
    def test1(self, input_data):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.find_element(By.ID, 'kw').send_keys(input_data[1])
        driver.quit()

    def test2(self):
        assert 2 == 1

    def test3(self):
        assert 2 == 2


if __name__ == '__main__':
    pytest.main(['-vs'])
