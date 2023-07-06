# -*- coding: utf-8 -*-            
# @Time : 2023/6/20 16:02
# @name : 黄谷芬
# @FileName: update_form.py
# @Software: PyCharm
import copy
import json
import allure
import requests
from api.request_data.form_req import FormReqParameter
from base.get_login_token import GetHeaders
from api.api.form_api.add_form import AddFormApi


class UpdateFormApi(AddFormApi, GetHeaders, FormReqParameter):
    @classmethod
    def update_form_api(self, request_data, use_assert=True):
        """
        修改物品信息 api
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
        with allure.step("请求地址：{};""请求参数：{}".format(self.get_base_url(0) + self.update_form_url(),
                                                                     request_data)):
            # 接口请求
            resp = requests.post(url=self.get_base_url(0) + self.update_form_url(), verify=False,
                                 headers=self.get_login_token_admin(), data=json.dumps(request_data))
        with allure.step("返回参数：{}".format(resp.json())):
            if use_assert:
                # 断言结果
                assert resp.json()["code"] == 200
            return resp

    def update_form(self):
        """填写物品信息-报价类"""
        formId = self.add_form_gujia().json()["data"]
        req_data = copy.deepcopy(self.update_form_data(formId))
        self.update_form_api(req_data)
        return formId
