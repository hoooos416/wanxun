# -*- coding: utf-8 -*-            
# @Time : 2023/6/25 11:21
# @name : 黄谷芬
# @FileName: test_confirm_price.py
# @Software: PyCharm
import allure

from api.api.form_api.confirm_price import ConfirmPriceApi


@allure.epic("表单中心-web")
@allure.feature("确认价格")
class TestConfirmPrice(ConfirmPriceApi):

    @allure.story("正向请求：确认价格")
    def test_confirm_price(self):
        self.confirm_price()