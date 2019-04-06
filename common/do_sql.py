# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 22:05
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : do_sql.py

from mysql import connector
from common import project_path
from common.readconfig import ReadConfig


class DoMsq:

    def my_sql(self, query, flag=1):
        """flag=1,代表返回一条SQL数据
           flag=2,代表返回多条SQL数据
        """
        db_config = ReadConfig().db_config()  # 获取数据库配置参数
        cnn = connector.connect(**db_config)  # 连接数据库
        cursor = cnn.cursor()  # 获取游标
        # query = 'select memberid from loan where Id =18366'  # 写SQL
        cursor.execute(query)  # 执行SQL 如果涉及到到增删改，需执行cursor.execute('commit')
        if flag == 1:
            res = cursor.fetchone()  # 获取一条SQL执行结果
        else:
            res = cursor.fetchall()  # 获取多条SQL执行结果
        return res
if __name__ == '__main__':
    query
        # 1125041	Miao 13800001113	1	518424.00	2019-03-16 16:20:51
