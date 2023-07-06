# -*- coding: utf-8 -*-            
# @Time : 2023/7/6 15:20
# @name : 黄谷芬
# @FileName: test_confirm_contact.py
# @Software: PyCharm
import allure
import pytest
from api.api.form_api.confirm_contact import ConfirmContactApi


@allure.epic("检测中心-APP")
@allure.feature("待确认-确认用户信息")
class TestConfirmContact(ConfirmContactApi):

    @allure.story("正向请求：待确认-确认用户信息：1个步骤（到店单")
    def test_confirm_contact_arrive(self):
        self.confirm_contact_arrive()