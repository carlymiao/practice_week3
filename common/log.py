#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 11:13
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : log.py
import logging
from common.readconfig import ReadConfig
from common import project_path


class Log:
    """此类引入日志模块"""

    def __init__(self):
        self.log_formatter = ReadConfig().log_formatter()
        self.log_level = ReadConfig().log_level()

    def log(self, level, msg):
        log = logging.getLogger('Log')
        log.setLevel(self.log_level)
        formatter = logging.Formatter(self.log_formatter)

        ch = logging.StreamHandler()
        ch.setLevel(self.log_level)
        ch.setFormatter(formatter)

        fh = logging.FileHandler(project_path.test_log_path, encoding='utf-8')
        fh.setLevel(self.log_level)
        fh.setFormatter(formatter)

        log.addHandler(ch)
        log.addHandler(fh)

        if level == 'debug':
            log.debug(msg)
        elif level == 'info':
            log.info(msg)
        elif level == 'warning':
            log.warning(msg)
        elif level == 'error':
            log.error(msg)
        else:
            log.critical(msg)

        log.removeHandler(ch)
        log.removeHandler(fh)

    @staticmethod
    def debug(msg):
        Log().log('debug', msg)

    @staticmethod
    def info(msg):
        Log().log('info', msg)

    @staticmethod
    def warning(msg):
        Log().log('warning', msg)

    @staticmethod
    def error(msg):
        Log().log('error', msg)

    @staticmethod
    def critical(msg):
        Log().log('critical ', msg)


if __name__ == '__main__':
    Log().debug('1')
    Log().info('2')
    Log().error('3')
    Log().warning('4')
    Log().critical('5')
