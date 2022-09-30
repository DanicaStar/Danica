'''
from selenium import webdriver
driver=webdriver.Chrome()  #打开谷歌浏览器
driver.get("https://www.baidu.com")    #访问被测网站
driver.find_element_by_xpath("//*[@id="kw"]").send_keys()   #输入框输入



中级：postman,linux,mysql,jemter
高级：自动化+框架+接口

自动化测试：
    1、自动化是什么：
        将重复性点点点转为为机器
        接口自动化
        UI自动化
        批量造数据、该数据
        监控，服务监控
    2、为什么自动化：
        敏捷开发，提高项目的迭代效率
        大面积回归
        冒烟测试
        测试报告
    3、如何实现自动化
        根据业务特点（接口、UI）
        根据业务的侧重点
        根据用例范围，选择合适的框架和语言
        执行策略，持续集成
测试框架：
    1、为什么搭建测试框架
        第三方开源技术框架：
            selenium，airtest,robotframework,applum,qtp,request
            语言+驱动框架+数据驱动+关键字驱动+代码分层
    2、为什么搭建自动化框架
        帮助自动化团队编写简单更好的维护用例，设计测试用例

接口测试：
    测试更早介入
    界面很难实现

Fiddle抓包详情
Fiddle篡改数据
Fiddle若亡测试

            
'''