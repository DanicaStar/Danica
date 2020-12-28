# -*- coding:utf-8 -*-
# @Time : 2020-12-22 19:03
# @Author: Danica
# @File : article_update.py

from myself_project.testcase.loginOk import TestLogin
import pytest
from time import sleep
class TestArticleUpdattle():
    def setup_class(self):
        #用户登录
        self.login=TestLogin
        self.login.userlogin(self)
        sleep(0.5)


    def testArticleUpdate(self):
        #点击我的文章
        self.driver.find_element_by_css_selector('#sidebar-menu > li:nth-child(4) > a > span:nth-child(2)').click()
        sleep(0.5)
        #点击文章列表
        self.driver.find_element_by_css_selector('#sidebar-menu > li.treeview.menu-open > ul > li:nth-child(1) > a').click()
        sleep(0.5)

        #点击文章标题
        self.driver.find_element_by_css_selector('body > div > div > section.content > div > div > div > div.box-body.no-padding > table > tbody > tr:nth-child(2) > td:nth-child(1) > strong > a').click()
        sleep(3)

        #获取文章标题输入框
        title=self.find_element_by_id('article-title')
        title.click()
        title.send_keys('小丸子')

        #进入frame
        loc1=self.driver.find_element_by_class_name('CodeMirror')
        loc1.send_keys('小丸子')


        # print(loc1.text)
        # self.driver.quit()
if __name__ == '__main__':
    pytest.main(['-sv','article_update.py'])
