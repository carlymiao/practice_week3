# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 12:09
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : project_path.py

import os

current_path = os.path.realpath(__file__)
# print(current_path)
# project_path = os.path.split(os.path.split(current_path)[0])[0]
# print(project_path)
test_cases_path = os.path.join(os.path.split(os.path.split(current_path)[0])[0], 'test_cases', 'testcase.xlsx')
test_report_path = os.path.join(os.path.split(os.path.split(current_path)[0])[0], 'test_result', 'test_report',
                                'test_result.html')
test_log_path = os.path.join(os.path.split(os.path.split(current_path)[0])[0], 'test_result', 'test_log',
                             'test_log.txt')

test_config_path = os.path.join(os.path.split(os.path.split(current_path)[0])[0], 'common', 'conf', 'config')

# print(test_config_path)
# print(test_report_path)
# print(test_log_path)
