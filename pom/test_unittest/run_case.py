'''
必须掌握测试套件和执行测试
1、添加测试套件
    确定测试用例文件夹的路径
    测试用例添加到测试套件中
2、执行测试
使用unittest自带的执行方式
    2.1 TextTestRunner()方法
    2.2 使用第三方插件执行测试 用例并生成测试报告（html）
        指定测试报告存放的位置
        命名测试报告名称
'''

import unittest
import time
# import HTMLTestRunner
# # 1、确定测试文件路径
# test_dir='./test_unittest'  #测试用例路径
# # 2、将测试用例添加到测试套件中
# discover=unittest.defaultTestLoader.discover(test_dir)
# # 3、使用unittest自带执行方式
# runner=unittest.TextTestRunner()
# # 4、执行测试套件中的测试用例
# runner.run(discover)

# 1、确定测试文件路径
test_dir='./test_unittest'  #测试用例路径
# 2、将测试用例添加到测试套件中
discover=unittest.defaultTestLoader.discover(test_dir)
# 3、指定测试报告存放的位置
report_dir='./report'
# 4、命名测试报告名称
now=time.strftime('%Y-%m-%d %H-%M-%S')
report_filename=report_dir+'/'+now+'report.html'  #测试报告路径+名称
stream=open(report_filename,'wb')
# 使用第三方插件执行并 生成测试报告
# runner=HTMLTestRunnerPlugins.HTMLTestRunner(
#     title='xxx自动化测试报告',
#     description = '登录注册页面自动化',
#     stream = stream
# )

# 5、执行测试套件中的测试用例
# runner.run(discover)
stream.close()