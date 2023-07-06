# -*- coding: utf-8 -*-            
# @Time : 2023/7/6 10:22
# @name : 黄谷芬
# @FileName: receive_form.py
# @Software: PyCharm

import copy
import allure
import requests
from api.api.form_api.dispatch import DispatchApi
from api.request_data.form_req import FormReqParameter
from base.get_login_token import GetHeaders
from base.mysql import Sql


class ReceiveFormApi(DispatchApi, GetHeaders, FormReqParameter, Sql):
    @classmethod
    def receive_form_api(self, request_data, form_id, use_assert=True):
        """
        检测师接单 api
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
        with allure.step("请求地址：{};""请求参数：{}".format(self.get_base_url(0) + self.receive_form_url(form_id),
                                                            request_data)):
            # 接口请求
            resp = requests.post(url=self.get_base_url(0) + self.receive_form_url(form_id), verify=False,
                                 headers=self.get_token_inspector(), json=request_data)
        with allure.step("返回参数：{}".format(resp.json())):
            if use_assert:
                # 断言结果
                assert resp.json()["code"] == 200
            return resp

    @classmethod
    def receive_arrive(self):
        """检测师接单-到店单"""
        formId = DispatchApi().dispatch_arrive()
        req = copy.deepcopy(self.receive_form_data())
        self.receive_form_api(req, formId, use_assert=False)
        conn = self.conn_mysql()
        sql = "select status, child_status from form where id =" + formId
        data = self.sql_select(conn, sql)
        assert (data[0] == 9 and data[1] == 7)
        self.sql_quit(conn)
        return formId
