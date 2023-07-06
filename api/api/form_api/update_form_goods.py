# -*- coding: utf-8 -*-            
# @Time : 2023/7/6 15:53
# @name : 黄谷芬
# @FileName: update_form_goods.py
# @Software: PyCharm
import copy
import allure
import requests

from api.api.form_api.confirm_contact import ConfirmContactApi
from api.request_data.form_req import FormReqParameter
from base.get_login_token import GetHeaders
from base.mysql import Sql


class UpdateFormGoodsApi(ConfirmContactApi, GetHeaders, FormReqParameter, Sql):
    @classmethod
    def update_form_goods_api(self, request_data, form_id, use_assert=True):
        """
        录入物品信息 api
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
        with allure.step("请求地址：{};""请求参数：{}".format(self.get_base_url(0) + self.update_form_goods_url(form_id),
                                                            request_data)):
            # 接口请求
            resp = requests.post(url=self.get_base_url(0) + self.update_form_goods_url(form_id), verify=False,
                                 headers=self.get_token_inspector(), json=request_data)
        with allure.step("返回参数：{}".format(resp.json())):
            if use_assert:
                # 断言结果
                assert resp.json()["code"] == 200
            return resp

    def update_form_goods_arrive(self):
        """待检测-录入物品信息（到店）"""
        formId = self.confirm_contact_arrive()
        req = copy.deepcopy(self.update_form_goods_data())
        resp = self.update_form_goods_api(req, formId, use_assert=False)
        conn = self.conn_mysql()
        sql = "select status, child_status from form where id =" + formId
        data = self.sql_select(conn, sql)
        assert (data[0] == 11 and data[1] == 2)
        self.sql_quit(conn)
        return formId