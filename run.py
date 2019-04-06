from test_cases.testcases import *  # 使用loader方法导入测试类，如模块中有好几个类，可以分别导入类
from test_cases import recharge
from test_cases import all_testcase_new
import HTMLTestRunnerNew
import unittest
import sys
sys.path.append('./')
print(sys.path)
suit = unittest.TestSuite()  # 实例化测试套件
loader = unittest.TestLoader()  # 参数化loader
report_path = project_path.test_report_path
# 匹配直接导入模块
# suit.addTest(loader.loadTestsFromModule(recharge))
suit.addTest(loader.loadTestsFromModule(all_testcase_new))

# 直接导入类
# suit.addTest(loader.loadTestsFromTestCase(TestCases))

with open(report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title='2019接口自动化',
                                              description=None,
                                              tester='Miao')
    runner.run(suit)

