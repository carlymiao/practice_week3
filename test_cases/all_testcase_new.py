#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:43
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : testcases.py
from common.http_request import HttpRequest
from common import project_path
from common.do_excel_new import DoExcel
from common.do_sql import DoMsq
from common.getdata import GetData
from common.readconfig import ReadConfig
from ddt import ddt, data
from common.log import Log
import unittest
import traceback

# 获取cookie的两种种方式：
# 1.定义全局变量，把cookie放到全局变量中
# 2.定义类变量

data_case = DoExcel(project_path.test_cases_path).read_excel()
cookie = None


@ddt
class TestCases(unittest.TestCase):
    """读取do_execl_new模块中用例，并执行用例"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*data_case)
    def test_cases(self, case):
        global test_result, cookie, before_amount
        url = case['Url']
        method = case['Method']
        param = case['Param']  # 如Param参数中，有id这个key
        if param.get('id'):
            param['id'] = getattr(GetData, 'loan_id')  # 把loan_id替换成id的value
        if param.get('mobilephone'):  # 把参数中的mobilephone参数化
            param['mobilephone'] = getattr(GetData, 'mobilephone')
        if param.get('pwd'):  # 把参数中的pwd参数化
            param['pwd'] = getattr(GetData, 'pwd')
        if param.get('memberId'):  # 把参数中的mobilephone参数化
            param['memberId'] = getattr(GetData, 'memberId')

        case_id = case['CaseId']
        module = case['Module']
        sql = case['Sql']
        if sql is not None:  # 把sql中的mobilephone参数化
            if sql.get('sql'):
                if sql['sql'].find('mobilephone') != -1:
                    sql['sql'] = sql['sql'].replace('mobilephone', str(getattr(GetData, 'mobilephone')))
        expected_result = case['ExpectedResult']
        if expected_result.get('data'):   #参数化excepect_result中的电话号码
            if expected_result['data'].get('mobilephone'):
                expected_result['data']['mobilephone'] = str(getattr(GetData, 'mobilephone')) #expect_result中mobilephone为str

        Log.info('--用例参数为{}'.format(case))
        if module == 'recharge' and case_id == 2 or module == 'add_loan' and case_id == 3:  # 查询投资和充值前的金额
            before_amount = DoMsq().my_sql(sql['sql'], 1)
        actual_result = HttpRequest().http_request(url, method, param, cookie)  # 返回 resp
        Log.info('--返回结果为:{}'.format(actual_result.json()))
        if actual_result.cookies:
            cookie = actual_result.cookies
        Log.info('---第{}条{}模块用例，返回结果{}---'.format(case_id, module, actual_result.text))
        # a=sql['sql']
        try:
            if module == 'add_loan' and case_id == 2:  # 取出加标后的loan_id
                loan_id = DoMsq().my_sql(sql['sql'], 1)
                setattr(GetData, 'loan_id', loan_id[0])

            if module == 'recharge' and case_id == 2:  # 查询充值后的金额
                after_charge = DoMsq().my_sql(sql['sql'], 1)  # sql是返回一个元组，元组中元素什么类型取决于数据库字段类型
                setattr(GetData, 'after_charge', after_charge[0])  # 赋值给after_charge是数字类型
                expected_result['data']['leaveamount'] = str(getattr(GetData, 'after_charge'))
                recharge_amount = getattr(GetData, 'after_charge') - int(before_amount[0])  # 充值金额=充值后的金额-充值前的金额
                self.assertEqual(recharge_amount, int(param['amount']))  # 判断数据库中充值后的金额是否正确

            if module == 'add_loan' and case_id == 3:  # 查询投资后的金额
                after_invest = DoMsq().my_sql(sql['sql'], 1)  # sql是返回一个元组，元组中元素什么类型取决于数据库字段类型
                setattr(GetData, 'after_invest', after_invest[0])
                invest_amount = before_amount[0] - getattr(GetData, 'after_invest')  # 投资金额=投资前的金额-投资后的金额
                self.assertEqual(invest_amount, int(param['amount']))  # 判断数据库中投资后的金额是否正确

            self.assertEqual(expected_result, actual_result.json())
            test_result = 'Pass'
        except Exception as e:
            test_result = 'Fail'
            Log().error(traceback.format_exc())
            raise e
        finally:
            Log.info('开始写回测试结果{}'.format(actual_result.json()))
            if module == 'recharge':
                DoExcel(project_path.test_cases_path).write_excel('recharge', case_id + 1, 9, actual_result.text)
                DoExcel(project_path.test_cases_path).write_excel('recharge', case_id + 1, 10, test_result)
            elif module in ('register', 'login'):
                DoExcel(project_path.test_cases_path).write_excel('Sheet1', case_id + 1, 8, actual_result.text)
                DoExcel(project_path.test_cases_path).write_excel('Sheet1', case_id + 1, 9, test_result)
            elif module == 'withdraw':
                DoExcel(project_path.test_cases_path).write_excel('withdraw', case_id + 1, 9, actual_result.text)
                DoExcel(project_path.test_cases_path).write_excel('withdraw', case_id + 1, 10, test_result)
            elif module == 'add_loan':
                DoExcel(project_path.test_cases_path).write_excel('add_loan', case_id + 1, 9, actual_result.text)
                DoExcel(project_path.test_cases_path).write_excel('add_loan', case_id + 1, 10, test_result)
            elif module in ('audit', 'invest'):
                DoExcel(project_path.test_cases_path).write_excel('audit', case_id + 1, 9, actual_result.text)
                DoExcel(project_path.test_cases_path).write_excel('audit', case_id + 1, 10, test_result)
