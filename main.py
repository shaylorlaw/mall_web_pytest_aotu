# @Time :2021-11-22 11:32
# @Author :ShaylorLaw
# @File :main.py

import unittest
from Common.dir_config import testcases_dir
from Common.dir_config import htmlreport_dir
import HTMLTestRunnerCN

#实例化套件对象
suite = unittest.TestSuite()
#TestLoader的用法
#1、实例化TestLoader对象
#2、使用discover去找到一个目录下的所有测试用例
#3、使用suite
loader = unittest.TestLoader()
suite.addTests(loader.discover(testcases_dir))
#运行
# runner = unittest.TextTestRunner()
# runner.run(suite)

with open(htmlreport_dir + \
                  '/autoTest_report.html','wb') as file:
    runner=HTMLTestRunnerCN.HTMLTestReportCN(stream=file,verbosity=2,title='web自动化测试报告',tester='Shaylor')
    runner.run(suite)
