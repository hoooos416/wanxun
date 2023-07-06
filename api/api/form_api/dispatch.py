# -*- coding: utf-8 -*-            
# @Time : 2023/7/5 16:41
# @name : 黄谷芬
# @FileName: dispatch.py
# @Software: PyCharm
import copy
import allure
import requests
from api.api.form_api.confirm_price import ConfirmPriceApi
from api.request_data.form_req import FormReqParameter
from base.get_login_token import GetHeaders
from base.mysql import Sql


class DispatchApi(ConfirmPriceApi, GetHeaders, FormReqParameter, Sql):
    @classmethod
    def dispatch_api(self, request_data, use_assert=True):
        """
        派单 api
        :param front:
        # :param base_url: 接口请求的服务地址
        :param request_data: 请求参数
        :param use_assert: 是否使用正常请求的断言
        :return:
        """
        # 该Api用于接口基础封装,封装时注意复用性
        # if front:
        #     # 报告写入是否为前置条件
        #     front_case_name = self.add_form_api.__doc__
        # allure步骤数据保存
        with allure.step("请求地址：{};""请求参数：{}".format(self.get_base_url(0) + self.dispatch_url(),
                                                            request_data)):
            # 接口请求
            resp = requests.post(url=self.get_base_url(0) + self.dispatch_url(), verify=False,
                                 headers=self.get_login_token_admin(), json=request_data)
        with allure.step("返回参数：{}".format(resp.json())):
            if use_assert:
                # 断言结果
                assert resp.json()["code"] == 200
            return resp

    def dispatch_arrive(self):
        """派单-到店单"""
        formId = self.confirm_price()
        req_data = copy.deepcopy(self.dispatch_arrive_data(formId))
        self.dispatch_api(req_data, use_assert=False)
        conn = self.conn_mysql()
        sql = "select status from form where id ="+formId
        data = self.sql_select(conn, sql)
        assert data[0]==6
        self.sql_quit(conn)
        return formId



