# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import urllib3
import json
from api.api.form_api.add_form import AddFormApi
import pytest
import os
import copy

import pytest


# class Test(object):
#
#     @pytest.mark.parametrize('sex', ['男', '女'])
#     @pytest.mark.parametrize('classes ', ['一班', '二班'])
#     @pytest.mark.parametrize('score', ['及格', '不及格'])
#     def test(self, sex, classes, score):
#         data = {'sex': '', 'classes': '', 'score': ''}
#         data['sex'] = sex
#         data['classes'] = classes
#         data['score'] = score
#         print(data)

if __name__ == '__main__':
    # 生成JSON数据,加上--clean-alluredir解决JSON文件生成冗余问题
    pytest.main(["-s", "--alluredir=outputs/reports/allure", "--clean-alluredir"])
    # 将JSON文件转换成HTML格式的测试报告（生成JSON文件路径：outputs/reports/allure; 生成HTML报告路径：outputs/reports/html）
    os.system("allure generate outputs/reports/allure -o outputs/reports/html --clean")
    # 命令：allure generate outputs/reports/allure -o outputs/reports/html --clean
    # 打开测试报告
    # os.system("allure serve outputs/reports/allure")
