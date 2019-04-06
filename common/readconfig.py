#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 11:30
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : readconfig.py

from configparser import ConfigParser
from common import project_path


class ReadConfig:
    """读取配置文件"""

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(project_path.test_config_path, encoding='utf-8')

    def log_formatter(self):
        log_formatter = self.cf.get('LOG', 'log_formatter')
        return log_formatter

    def log_level(self):
        log_level = self.cf.get('LOG', 'log_setLevel')
        return log_level

    # [CASE]
    # case_amount = {'recharge': 0, 'Sheet1': [1, 3, 5]}

    def case_amount(self):
        case_amount = self.cf.get('CASE', 'case_amount')
        return eval(case_amount)

    def db_config(self):
        db_config = self.cf.get('DB', 'db_config')
        return eval(db_config)


if __name__ == '__main__':
    formatter = ReadConfig().case_amount()
    level = ReadConfig().log_level()
    amount = ReadConfig().case_amount()
    print(formatter, level, amount)
