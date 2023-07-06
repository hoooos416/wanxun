# -*- coding: utf-8 -*-            
# @Time : 2023/7/6 16:03
# @name : 黄谷芬
# @FileName: test_update_goods.py
# @Software: PyCharm
import allure
import pytest
from api.api.form_api.update_form_goods import UpdateFormGoodsApi


@allure.epic("检测中心-APP")
@allure.feature("待检测-录入物品信息")
class TestUpdateGoods(UpdateFormGoodsApi):

    @allure.story("正向请求：待检测-录入物品信息（到店单")
    def test_update_form_goods_arrive(self):
        self.update_form_goods_arrive()
