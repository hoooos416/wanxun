# -*- coding: utf-8 -*-            
# @Time : 2023/7/5 17:14
# @name : 黄谷芬
# @FileName: test_dispatch.py
# @Software: PyCharm

import allure
import pytest
from api.api.form_api.dispatch import DispatchApi


@allure.epic("表单中心-web")
@allure.feature("客服派单")
class TestDispatch(DispatchApi):

    @allure.story("正向请求：派单-到店单")
    def test_dispatch_arrive(self):
        self.dispatch_arrive()