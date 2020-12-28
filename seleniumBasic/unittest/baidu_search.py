'''
  Code description：
  Create time：
  Developer：
'''
# -*- coding: utf-8 -*-
import time
import unittest
from selenium import webdriver
class Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        测试前置条件，这里要搜索的话就是先得打开百度网站啦
        """
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.driver.get("https://www.baidu.com")
    @classmethod
    def tearDownClass(cls):
        """
        测试结束后环境复原，这里就是浏览器关闭退出
        """
        cls.driver.quit()
    def test_search1(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        """
        self.driver.find_element_by_id('kw').send_keys('python2')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        try:
            assert 'python2' in self.driver.title
            print('检索python2完成')
        except Exception as e:
            print('检索失败', format(e))
    def test_search2(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        """
        self.driver.find_element_by_id('kw').clear()              # 清空之前输入的python2
        self.driver.find_element_by_id('kw').send_keys('python3')
        self.driver.find_element_by_id('su').click()
        time.sleep(1)
        try:
            assert 'python3' in self.driver.title
            print('检索python3完成')
        except Exception as e:
            print('检索失败', format(e))
if __name__ == '__main__':
    unittest.main()


