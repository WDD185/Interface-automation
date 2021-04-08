import allure
import jsonpath
from script.ji_yun_ying_pc.data_config.data_config import order_infos
from script.base_api.service_education import *
from script.base_api.api_operation_web import *
from script.base_api.service_user.employees import *
from script.default_header import jyy_header


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
        student_id = order_info.get("student_id")
        school_area_id = order_info.get("school_area_id")
        subject = order_info.get("subject")

        # 查询班级
        params = "pageNum=1&pageSize=10"
        body = {'courseType': '常规班课', 'schoolArea': school_area_id, 'year': '2021', 'term': '暑', 'subject': subject}
        res = education_classes_order_query_post(params, body=body, header=jyy_header)
        class_list = jsonpath.jsonpath(res, "$.data.content")
        class_info = get_class_info(class_list)
        if class_info:
            class_id = class_info.get("classId")
            class_total_price = int(float(class_info.get("totalPrice")))
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
            body = {'orderId': order_id, 'operatorId': employee_id, 'operatorType': 'STAFF', 'remark': '', 'payInfos': [{'payChannel': 'CASH', 'payAmount': class_total_price}]}
            pay_post(body=body, header=jyy_header)




