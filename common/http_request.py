# -*- coding: utf-8 -*-
# @Time    : 2019/3/17 19:08
# @Author  : Miao
# @Email   : 3266565259@qq.com
# @File    : http_request.py
import requests
from common.log import Log


class HttpRequest:
    """ 该类完成http的get以及post请求，并返回结果"""

    def http_request(self, url, method, param, cookie):
        global resp
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param, cookies=cookie)
                # print(resp)
                # print(resp.text)
                # print(resp.json())

            except Exception as e:
                Log.error('GET请求出错啦{}'.format(e))
        elif method.upper() == 'POST':
            try:
                resp = requests.post(url, data=param, cookies=cookie)
                # result = resp.text()
            except Exception as e:
                Log().error('POST请求出错啦{}'.format(e))
        else:
            print('不支持该方法')
        return resp
        # 此处直接返回resp,后期需要resp.text还是resp.json()可自行选择


if __name__ == '__main__':
    t = HttpRequest()
    t.http_request('http://47.107.168.87:8080/futureloan/mvc/api/member/login', 'GET',
                   {'mobilephone': '13800001113', 'pwd': '123456'})
