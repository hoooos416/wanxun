# -*- coding: utf-8 -*-            
# @Time : 2023/3/20 18:11
# @name : 黄谷芬
# @FileName: get_login_token.py
# @Software: PyCharm
from api.request_data.form_req import FormReqParameter
from base.url import UrlParameter
import requests
import urllib3


class GetHeaders(UrlParameter, FormReqParameter
                 ):

    @classmethod
    def get_login_token_admin(self):
        """超管号登录"""
        urllib3.disable_warnings()  # 过滤警告
        res1 = requests.get(url=self.get_base_url(0) + self.login_web_url(),
                            verify=False)
        token = res1.json()['data']['accessToken']
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        return headers

    @classmethod
    def get_token_inspector(self):
        """检测师登录"""
        urllib3.disable_warnings()  # 过滤警告
        res = requests.get(url=self.get_base_url(0) + self.login_app_url(),
                           verify=False)
        token = res.json()['data']['accessToken']
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        return headers
