# -*- coding:utf-8 -*-
# @Time : 2020-11-23 19:19
# @Author: Danica
# @File : test_TestCategory.py

from time import sleep
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pythonProject.testcases.pytest.test_admin_login import TestAdminLogin
import pytest

class TestCategory(object):
    def setup_class(self):
        self.login=TestAdminLogin()

    #测试文章分类失败，名称为空
    @pytest.mark.dependency(depemds=['admin_login'],scope='module')
    def test_add_category_error(self):
        name=''
        parent='python'
        slug='test'
        expected='分类名称不能为空'

        #点击菜单文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)

        #点击菜单分类
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)

        #输入分类名称
        self.login.driver.find_element_by_name('category.title').send_keys(name)

        #选择父分类
        parent_category_elem=self.login.driver.find_element_by_name('category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        #输入slug
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        #点击添加
        self.login.driver.find_element_by_xpath('/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        loc=(By.CLASS_NAME,'toast-message')
        WebDriverWait(self.login.driver,5).until(EC.visibility_of_element_located(loc))

        msg=self.login.driver.find_element(*loc).text

        assert  msg==expected


    #测试文章分类成功
    def test_add_category_ok(self):
        name = 'test'
        parent = 'python'
        slug = 'test'
        expected = None

        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)

        # 点击分类
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[3]/a').click()
        sleep(1)

        # 输入分类名称
        self.login.driver.find_element_by_name('category.title').send_keys(name)

        # 选择父分类
        parent_category_elem = self.login.driver.find_element_by_name('category.pid')
        Select(parent_category_elem).select_by_visible_text(parent)

        # 输入slug
        self.login.driver.find_element_by_name('category.slug').send_keys(slug)

        # 点击添加
        self.login.driver.find_element_by_xpath(
            '/html/body/div/div/section[2]/div/div[1]/div/form/div[2]/div/div/button').click()

        assert 1== 1

if __name__ == '__main__':
    pytest.main(['-sv', 'test_TestCategory.py'])