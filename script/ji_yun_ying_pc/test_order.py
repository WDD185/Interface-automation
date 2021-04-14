import allure
import jsonpath
from script.ji_yun_ying_pc.data_config.data_config import order_infos, school_areas
from script.base_api.service_education import *
from script.base_api.api_operation_web import *
from script.base_api.service_user.employees import *
from script.default_header import jyy_header
import time
import pytest


def get_class_info(class_list):
    if class_list:
        class_list = [x for x in class_list[0] if (int(x.get("classStudentNum")) - int(x.get("attendStudentNum"))) > 0]
    if class_list:
        return class_list[0]


@allure.feature("极运营PC订单业务")
class TestOrder:

    @allure.story("极运营PC下单")
    @pytest.mark.parametrize("order_info", order_infos)
    def test_order(self, order_info):
        student_id = order_info.get("studentId")
        school_area_id = order_info.get("schoolAreaId")
        subject = order_info.get("subject")

        # 查询班级
        params = "pageNum=1&pageSize=100"
        body = {'courseType': '常规班课', 'schoolArea': school_area_id, 'year': '2021', 'term': '暑', 'subject': subject}
        res = education_classes_order_query_post(params, body=body, header=jyy_header)
        class_list = jsonpath.jsonpath(res, "$.data.content")
        class_info = get_class_info(class_list)
        if class_info:
            class_id = class_info.get("classId")
            class_total_price = float(class_info.get("totalPrice"))
            class_num = int(float(class_info.get("coursePeriod")))

            # 获取用户信息
            params = {"token": jyy_header.get("Authorization").replace("Bearer ", "")}
            res_json = employees_info_get(params=params, header=jyy_header)
            employee_ids = jsonpath.jsonpath(res_json, "$..employeeId")
            employee_id = employee_ids[0] if employee_ids else "not found"

            # 下单
            params = "recommit-ticket=undefined"
            body = {'studentId': student_id,
                    'schoolArea': int(school_area_id),
                    'details': [{'classId': class_id, 'num': class_num, 'discountId': '', 'category': 'CLASS'}],
                    'discounts': [],
                    'epayAmount': 0,
                    'amount': class_total_price,
                    'remark': '',
                    'couponItemIds': []
                    }
            res = order_saveOrder_post(params, body=body, header=jyy_header)
            order_ids = jsonpath.jsonpath(res, "$.data")
            order_id = order_ids[0] if order_ids else None

            # 支付订单
            if order_id:
                body = {'orderId': order_id,
                        'operatorId': employee_id,
                        'operatorType': 'STAFF',
                        'remark': '',
                        'payInfos': [{'payChannel': 'CASH', 'payAmount': class_total_price}]
                        }
                pay_post(body=body, header=jyy_header)
                time.sleep(0.5)

    # @allure.story("极运营订单作废")
    # @pytest.mark.parametrize("school_area_id", school_areas)
    # def test_order(self, school_area_id):
    #
    #     # 查询已完成订单
    #     body = {
    #         "pageSize": 300,
    #         "pageNum": 1,
    #         "schoolAreas": [school_area_id],
    #         "status": "PAID",
    #         "startCreateTime": "2021-04-09 00:00:00",
    #         "endCreateTime": "2021-04-09 23:59:59"
    #     }
    #     res = order_query_post(body=body, header=jyy_header)
    #     order_list = jsonpath.jsonpath(res, "$.data.list")
    #     if order_list:
    #         order_list = [x.get("id") for x in order_list[0]]
    #
    #         # 获取用户信息
    #         params = {"token": jyy_header.get("Authorization").replace("Bearer ", "")}
    #         res_json = employees_info_get(params=params, header=jyy_header)
    #         employee_ids = jsonpath.jsonpath(res_json, "$..employeeId")
    #         employee_id = employee_ids[0] if employee_ids else "not found"
    #         employee_names = jsonpath.jsonpath(res_json, "$..employeeName")
    #         employee_name = employee_names[0] if employee_names else "not found"
    #         for order_id in order_list:
    #
    #             # 订单作废
    #             if order_id:
    #                 params = f"orderId={order_id}&seat=2&operater={employee_name}&operaterId={employee_id}"
    #                 order_scrapOrder_get(params=params, header=jyy_header)
    #                 time.sleep(0.1)



