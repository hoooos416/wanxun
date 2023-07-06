# -*- coding: utf-8 -*-            
# @Time : 2023/7/6 15:21
# @name : 黄谷芬
# @FileName: test_receive_form.py
# @Software: PyCharm

import allure
import pytest
from api.api.form_api.receive_form import ReceiveFormApi


@allure.epic("检测中心-APP")
@allure.feature("检测师接单")
class TestReceiveForm(ReceiveFormApi):

    @allure.story("正向请求：检测师接单-到店单")
    def test_receive_arrive(self):
        self.receive_arrive()