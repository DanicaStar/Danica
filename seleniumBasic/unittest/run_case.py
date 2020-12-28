'''
  Code description： 执行add 的测试用例集
  Create time：
  Developer：
'''
# -*- coding: utf-8 -*-
from seleniumBasic.unittest.baidu_search import Search   # 将baidu_sreach.py模块导入进来
import unittest
 
suite = unittest.TestSuite()        # 构造测试用例集
# suite.addTest(Search("test_search1"))
suite.addTest(Search("test_search2"))     # 分别添加baidu_sreach1.py中的两个检索的测试用例
 
if __name__ == '__main__':
    runner = unittest.TextTestRunner()   # 实例化runner
    runner.run(suite)                   #执行测试



