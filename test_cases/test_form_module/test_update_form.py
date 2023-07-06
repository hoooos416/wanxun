# -*- coding: utf-8 -*-            
# @Time : 2023/6/20 16:37
# @name : 黄谷芬
# @FileName: test_update_form.py
# @Software: PyCharm
import allure
import pytest
from api.api.form_api.update_form import UpdateFormApi
import copy
import os


@allure.epic("表单中心-web")
@allure.feature("填写物品信息")
class TestUpdateForm(UpdateFormApi):

    @allure.story("正向请求：填写物品信息")
    def test_update_form(self):
        self.update_form()