# -*- coding:utf-8 -*-
# @Time : 2020-10-27 21:10
# @Author: Danica
# @File : test_category.py

from time import sleep
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestArticle():
    def __init__(self,login):
        self.login=login

    #测试文章分类失败，名称为空
    def test_add_article_ok(self):
        title='我的文章'
        content='我的文章内容'
        expected='文章保存成功'

        #点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)

        #点击写文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        sleep(1)

        #输入文章标题
        self.login.driver.find_element_by_id('article-title').send_keys(title)

        #进入frame
        frame1=self.login.driver.find_element_by_class_name("cke_wysiwyg_frame cke_reset")
        self.login.driver.switch_to.frame(frame1)
        sleep(1)

        #输入文章内容
        self.login.driver.find_element_by_xpath('/html/body/p').send_keys(content)

        #跳出frame
        self.login.driver.switch_to.default_contert()

        #点击发布
        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()



        loc=(By.CLASS_NAME,'toast-message')
        WebDriverWait(self.login.driver,5).until(EC.visibility_of_element_located(loc))

        msg=self.login.driver.find_element(*loc).text

        assert  msg==expected


    #测试删除文章分类成功
    def test_delete_article_ok(self):

        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)

        # 点击文章管理
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        # 定位到文章链接，移动到文章链接上
        link=self.login.driver.find_element_by_xpath('/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/strong/a')

        ActionChains(self.login.driver).move_to_element(link).perform()
        sleep(1)

        #删除文章数
        article_num=len(self.login.driver.find_element_by_class_name('jp-actiontr'))
        del_elem=self.login.driver.find_element_by_xpath('/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[2]/td[2]/div/div/a[2]')
        del_elem.click()
        sleep(1)

        #删除后文章数
        article_num2 = len(self.login.driver.find_element_by_class_name('jp-actiontr'))
        assert article_num==article_num2+1

    #删除所有文章
    def test_delete_all_article_ok(self):
        #点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)

        # 点击文章管理
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[1]/a').click()
        sleep(1)

        #定位全选
        link=self.login.driver.find_element_by_xpath('/html/body/div/div/section[3]/div/div/div/div[2]/table/tbody/tr[1]/td[1]/input')
        link.click()

        #点击批量删除
        self.login.driver.find_element_by_id('batchDel').click()
        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located())
        alert =self.login.driver.switch_to.alert
        alert.accept()

        sleep(1)

        article_num=self.login.driver.find_element_by_class_name('jp-actiontr')
        assert len(article_num)==0

if __name__ == '__main__':
    testArticle=TestArticle()
    testArticle.test_add_article_ok()







