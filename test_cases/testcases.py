#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:43
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : testcases.py
from common.http_request import HttpRequest
from common import project_path
from common.do_excel import DoExcel
from ddt import ddt, data
from common.log import Log
import unittest

data_case = DoExcel(project_path.test_cases_path).read_excel('Sheet1', 'Sheet1')


@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*data_case)
    def test_cases(self, case):
        global test_result
        url = case['Url']
        method = case['Method']
        param = case['Param']
        case_id = case['CaseId']
        module = case['Module']
        expected_result = case['ExpectedResult']
        Log.info('用例参数为{}'.format(case))
        actual_result = HttpRequest().http_request(url, method, param)  # 返回 resp
        Log.info('第{}条{}模块用例，返回结果{}'.format(case_id, module, actual_result.json()))
        try:
            self.assertEqual(expected_result, actual_result.json())
            test_result = 'Pass'
        except Exception as e:
            test_result = 'Fail'
            Log.error(e)
            raise e
        finally:
            Log().info('-----------------------------------------开始写回测试结果-----------------------------------------')
            DoExcel(project_path.test_cases_path).write_excel('Sheet1', case_id + 1, 8, actual_result.text)
            DoExcel(project_path.test_cases_path).write_excel('Sheet1', case_id + 1, 9, test_result)
