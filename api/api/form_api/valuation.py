# -*- coding: utf-8 -*-            
# @Time : 2023/6/26 11:35
# @name : 黄谷芬
# @FileName: valuation.py
# @Software: PyCharm
import copy
import json
import allure
import requests

from api.api.form_api.inquire_status import InquireFormApi
from api.api.form_api.update_form import UpdateFormApi
from api.request_data.form_req import FormReqParameter
from base.get_login_token import GetHeaders


class ValuationApi(UpdateFormApi, InquireFormApi, GetHeaders, FormReqParameter):
    @classmethod
    def valuation_api(self, request_data, use_assert=True):
        """
        申请核价 api
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
        with allure.step("请求地址：{};""请求参数：{}".format(self.get_base_url(0) + self.valuation_url(),
                                                                     request_data)):
            # 接口请求
            resp = requests.post(url=self.get_base_url(0) + self.valuation_url(), verify=False,
                                 headers=self.get_login_token_admin(), data=json.dumps(request_data))
            formId =resp.json()["formId"]
        with allure.step("返回参数：{}".format(resp.json())):
            if use_assert:
                # 断言结果
                req = copy.deepcopy(self.inquire_form_data(formId))
                self.inquire_form_api()
                assert resp.json()["code"] == 200 and

            return resp

    def valuation(self):
        """申请核价"""
        formId = self.update_form()
        req_data = copy.deepcopy(self.confirm_price_data(formId))
        self.valuation_api(req_data)