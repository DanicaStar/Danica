# -*- coding: utf-8 -*-
# @Time    : 2022/9/23 10:20 上午
# @Author  : danica
# @FileName: run_case.py
# @Software: PyCharm

"""
1、添加测试套件
    1.1、确定测试文件夹的路径
    1.2、将测试用例添加到测试套件中
2、执行测试用例
    2.1、使用unittest自带执行方式
        TextTestRunner() 方法
    2.2、使用第三方插件执行测试用例并且可生产测试报告(HTML)
        指定测试报告存放位置
        命名测试报告的名称
"""

import unittest
import time
import pytest
import pytest_html

# import HTMLTestRunnerPlugins

# # 1、确定测试文件路径
# test_dir = '../script'
# # 2、将测试用例添加到测试套件中
# discover = unittest.defaultTestLoader.discover(test_dir)
# # 3、使用unittest自带执行方式
# runner = unittest.TextTestRunner()
# # 4、执行测试套件中的测试用例
# runner.run(discover)

if __name__ == '__main__':
    # 单个文件运行，多个的时候将文件添加到列表中
    # pytest.main(['../test_ddt.py'])
    # 运行整个目录
    pytest.main(['./script', '--alluredir', './report/reportallure'])

# # 3、指定测试报告存放位置
# report_dir = './report'
# # 4、命名测试报告的名称
# now = time.strftime('%Y-%m-%d %H_%M_%S')
# report_name = report_dir + '/' + now + 'report.html'  # 测试报告路径+名称
# stream = open(report_name, 'wb')
# # 5、使用第三方包
# runner = HTMLTestRunnerPlugins(
#     title='ECShop自动化测试报告',
#     description='登陆注册页面自动化',
#     stream=stream
# )
# runner.run(discover)
# stream.close()
