# -*- coding: utf-8 -*-            
# @Time : 2023/3/15 22:40
# @name : 黄谷芬
# @FileName: url.py
# @Software: PyCharm
class UrlParameter(object):

    @classmethod
    def get_base_url(cls, type):
        """
        各个环境地址
        0：万循web测试环境
        1：万循app测试环境
        -------------
        2：万循web线上环境
        3：万循app线上环境
        :return:
        """
        if type == 0:
            return "https://wxapidev.jiumao100.com"

    @classmethod
    def login_web_url(cls):
        """
        登录web端
        :return:
        """
        return "/user/pc/user/login?username=15859122529&password=123456"

    @classmethod
    def login_app_url(cls):
        """
        登录APP端
        :return:
        """
        return"/user/app/user/login?username=15859122530&password=123456&id=100d85590856ff39d2c&type=1"

    @classmethod
    def add_form_url(cls):
        """
        新增表单
        :return:
        """
        return "/form/pc/form/v2/add"

    @classmethod
    def update_form_url(cls):
        """
        修改物品信息
        :return:
        """
        return "/form/pc/form/v2/update"

    @classmethod
    def confirm_price_url(cls):
        """
        确认价格
        :return:
        """
        return "/form/pc/form/v2/confirmPrice"

    @classmethod
    def valuation_url(cls):
        """
        申请核价
        :return:
        """
        return "/form/pc/form/v2/userValuation"

    @classmethod
    def dispatch_url(cls):
        """
        派单
        :return:
        """
        return "/form/pc/form/dispatch"

    @classmethod
    def inquire_form_url(cls):
        """
        查询表单
        :return:
        """
        return "/form/pc/form/getPageByParam"

    # =====================================检测师端================================================

    @classmethod
    def receive_form_url(cls, formId):
        """
        检测师接单
        :return:
        """
        return "/form/app/form/v2/detectionUserTakeForm?formId=" + formId

    @classmethod
    def confirm_contact_url(cls, formId):
        """
        待确认-确认用户信息：1个步骤
        :param formId:
        :return:
        """
        return "/form/app/form/v2/businessConfirmTransact/"+formId

    @classmethod
    def update_form_goods_url(cls, formId):
        """
        录入物品信息
        :param formId:
        :return:
        """
        return "/form/app/form/v2/businessUpdateFormGoods/"+formId