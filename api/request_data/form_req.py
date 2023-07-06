# -*- coding: utf-8 -*-            
# @Time : 2023/3/15 23:15
# @name : 黄谷芬
# @FileName: form_req.py
# @Software: PyCharm
import json
from api.request_data.form_req_index import FormReqDataIndex


class FormReqParameter(FormReqDataIndex):


    @classmethod
    def add_form_gujia_data(cls, typeId):
        """新建估价类表单"""
        return {
            "channelId": "1503552431321837569",
            "phone": "15892037169",
            "area": "广东省/广州市/天河区",
            "address": "",
            "goods": {
                cls.typeId: typeId,
                "brand": "iphone16",
                "modelNumber": "hgf123",
                "serialNumber": "hgf1234",
                "color": "紫色",
                "size": "256G",
                "remark": "完美无瑕疵",
                "images": [
                    "https://osstest.jiumao100.com/wanxun-form/b9201e6a-c1dc-47ea-f4a4-81ae2ad824dd-lxikm"
                ]
            },
            "nickName": ""
        }

    def update_form_data(cls, formId):
        """修改物品信息"""
        return {
             cls.formId: formId,
             "goods": {
                "typeId": "1534841578171502594",
                "brand": "iphone16",
                "modelNumber": "hgf123",
                "serialNumber": "hgf1234",
                "color": "紫色",
                "size": "256G",
                "remark": "完美无瑕疵",
                "images": [
                    "https://osstest.jiumao100.com/wanxun-form/b9201e6a-c1dc-47ea-f4a4-81ae2ad824dd-lxikm"
                ]
            }
        }

    def confirm_price_data(cls, formId):
        """修改物品信息"""
        return {
            cls.formId: formId,
            "recyclingPrice": 550000,
            "transactType": 0,
            "storageDays": 0,
            "depositPrice": 525000,
            "depositServiceFee": 29000,
            "compareCredentialsImage": "https://osstest.jiumao100.com/wanxun-form/42134f4b-d982-45f9-9107-e5b4b30dc94c-qxyuh"
        }

    def valuation_data(cls, formId):
        """修改物品信息"""
        return {
            "compareCredentialsImage": "",
            "comparePricesInfo": [
            ],
            "depositPrice": 762000,
            "depositServiceFee": 36800,
            cls.formId: formId,
            "recyclingPrice": 800000,
            "remark": "",
            "storageDays": 0,
            "transactMethod": 0,
            "transactType": 0,
            "userPrice": 0
        }

    def inquire_form_data(cls, formId):
        """查询表单状态"""
        return {
            "current": 1,
            "size": 10,
            "data": {
                "param": formId
            }
        }

    @classmethod
    def dispatch_arrive_data(cls, formId):
        """"派单-到店"""
        return {
            cls.formId: formId,
            "storesId": "4007445",
            "transactMethod": 0,
            "dealWayInformation": {
                "onShop": {
                    "name": "",
                    "phone": "15892037169",
                    "area": "广东省/广州市/海珠区",
                    "address": "海珠",
                    "time": 1688553670000
                }
            }
        }
    #=====================================检测师接单================================================

    @classmethod
    def receive_form_data(cls):
        """检测师接单"""
        return{}

    @classmethod
    def confirm_contact_data(cls):
        """待确认-确认用户信息：1个步骤"""
        return {"type": None, "time": 1688627741731, "addFormContactDto": {"type": 0, "pass": 1,
                                                                           "content": "D令K/s*A回11：05<待确认订单信息核价记录待确认00：16：441任务：确认办理信息确认办理客户信息手机号：19867580312复制拨打电话姓名：黄谷芬联系方式提示：还没有用户的联系方式，需添加用户的联系方式方可确认信息+添加联系方式联系记录发送短信联系类型：服务码聊天或短信图片提示：需上传与客户真实的聊天截图或发送短信后具有短信内容的截图上传你和客户联系凭证，图片中厂需包含以下任一关键词1.用户手机号后四位2.用户名字3.订单号确认信息",
                                                                           "image": "https://osstest.jiumao100.com/wanxun-form/f34679aa-b183-4fa5-f74c-ec6423fbecf9"}}

    @classmethod
    def update_form_goods_data(cls):
        """录入物品信息"""
        return {"typeId": "1534841578171502594", "brand": "测试机", "modelNumber": "自动化测试",
                "serialNumber": "自动化123", "color": "blue", "size": "256G",
                "remark": "此物品为本人合法所有，如有不实愿承担一切法律责任",
                "images": ["https://osstest.jiumao100.com/wanxun-form/8eca2996-0db2-49f7-f4bc-62b727cb9c0d",
                           "https://osstest.jiumao100.com/wanxun-form/74d82d3d-b651-49a3-d547-266a2e1acda5",
                           "https://osstest.jiumao100.com/wanxun-form/24973ce0-278a-4ee4-a4b1-ff7ce2d709eb",
                           "https://osstest.jiumao100.com/wanxun-form/766457ee-7535-416c-b77c-d383e41f59af",
                           "https://osstest.jiumao100.com/wanxun-form/b19b8796-6b4d-48ad-a974-6b79baabb605"]}
