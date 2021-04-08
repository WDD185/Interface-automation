
import pytest
import allure
import jsonpath
from script.base_api.service_profile import *
from script.base_api.api_operation_web import *
from script.base_api.service_finance import *
from script.base_api.service_pay import *
from script.base_api.service_education import *


@allure.feature("待修改")
@allure.testcase("待修改")
class AutoCreate:

    @allure.story("待修改")
    def test_auto_create(self):
        
        params = "pageNum=1&pageSize=10&studentName=%E8%AF%BE%E6%B6%88&phoneNum=&schoolAreaId=2369&usePosition=signUp"
        body = None
        res = students_studentInfo_get(params, body=body)
        

        params = "studentId=10153408"
        body = None
        res = students_check_message_get(params, body=body)
        

        params = ""
        body = {'studentId': 10153408}
        res = v2_finance_query_student_school_account_post(params, body=body)
        

        params = "type=campus"
        body = None
        res = system_setting_query_get(params, body=body)
        

        params = "pageNum=1&pageSize=10"
        body = {'courseType': '常规班课', 'schoolArea': '2369', 'year': '2021', 'term': '暑', 'grade': '四年级', 'subject': '数学'}
        res = education_classes_order_query_post(params, body=body)
        

        params = "pageNum=1&pageSize=10"
        body = {'courseType': '常规班课', 'schoolArea': '2369', 'year': '2021', 'term': '暑', 'subject': '数学'}
        res = education_classes_order_query_post(params, body=body)
        

        params = ""
        body = None
        res = classes_classId_seats_get(100131912, params, body=body)
        

        params = ""
        body = {'studentId': '10153408', 'classIds': [100131912], 'pcPreValid': True}
        res = orderFlow_preValidOrderCondition_post(params, body=body)
        

        params = ""
        body = {'classIds': [100131912], 'studentId': 10153408}
        res = orderFlow_queryMatchDiscountAndCoupon_post(params, body=body)
        

        params = ""
        body = {'details': [{'classId': 100131912, 'num': 25, 'coursePrice': '68.00', 'totalPrice': '1700.00', 'coursePeriod': '25.0'}], 'coupons': [], 'discounts': []}
        res = orderFlow_calculateOrderPrice_post(params, body=body)
        

        params = ""
        body = {'details': [{'classId': 100131912, 'num': 25, 'coursePrice': '68.00', 'totalPrice': '1700.00', 'coursePeriod': '25.0'}], 'coupons': [], 'discounts': []}
        res = orderFlow_calculateOrderPrice_post(params, body=body)
        

        params = "recommit-ticket=undefined"
        body = {'studentId': 10153408, 'schoolArea': 2369, 'details': [{'classId': 100131912, 'num': 25, 'discountId': '', 'category': 'CLASS'}], 'discounts': [], 'epayAmount': 0, 'amount': 1700, 'remark': '', 'couponItemIds': []}
        res = order_saveOrder_post(params, body=body)
        

        params = "orderId=854750&orderDetailId="
        body = None
        res = order_queryOrderDetail_get(params, body=body)
        

        params = "schoolArea=2369"
        body = None
        res = pay_boc_pos_posInfo_get(params, body=body)
        

        params = ""
        body = {'orderId': '854750', 'operatorId': 8223, 'operatorType': 'STAFF', 'remark': '', 'payInfos': [{'payChannel': 'CASH', 'payAmount': 1700}]}
        res = pay_post(params, body=body)
        

        params = "orderId=854750&orderDetailId="
        body = None
        res = order_queryOrderDetail_get(params, body=body)
        
        
