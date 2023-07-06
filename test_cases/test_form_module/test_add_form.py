# -*- coding: utf-8 -*-            
# @Time : 2023/3/25 11:06
# @name : 黄谷芬
# @FileName: test_add_form.py
# @Software: PyCharm
import allure
import pytest

import copy
import os

from api.api.form_api.add_form import AddFormApi


@allure.epic("表单中心-web")
@allure.feature("新建表单")
class TestAddForm(AddFormApi):

    @allure.story("正向请求：新建估价类表单")
    def test_add_form_gujia(self):
        self.add_form_gujia()

    @allure.story("正向请求：新建报价类表单")
    def test_add_form_baojia(self):
        self.add_form_baojia()

    @allure.story("参数channelId类型为非str类型的异常组合")
    @pytest.mark.parametrize("param1", [123, 12.3, [999]])
    def test_params_type_str_error(self, param1):
        req_data = copy.deepcopy(self.add_form_gujia_data(typeId="1534841578171502594"))
        req_data["channelId"] = param1
        resp = self.add_form_api(req_data, use_assert=False)
        assert resp.json()["code"] == 400, "channelId参数类型异常校验失败"

    @allure.story("参数phone类型为非str类型的异常组合")
    @pytest.mark.parametrize("param2", [123, 12.3, [999]])
    def test_params_type_str2_error(self, param2):
            req_data = copy.deepcopy(AddFormApi().add_form_gujia_data(typeId="1534841578171502594"))
            req_data["phone"] = param2
            resp = self.add_form_api(req_data, use_assert=False)
            assert resp.json()["code"] == 400, "channelId参数类型异常校验失败"


