
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/订单/单买订单列表")
def applet_order_orderListForSingle_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/orderListForSingle"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/单买下单")
def applet_order_saveOrder_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/购课单列表")
def applet_getPurchaseOrderList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/applet/getPurchaseOrderList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/购课单数量")
def applet_purchaseOrder_studentId_student_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/applet/purchaseOrder/{studentId}/student/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/添加购课单")
def applet_purchaseOrder_studentId_student_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/applet/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/删除购课单")
def applet_purchaseOrder_studentId_student_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/applet/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/班级座次")
def applet_classes_classId_seats_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/applet/classes/{classId}/seats"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/电子钱包余额")
def applet_financial_wallet_remain_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/applet/financial/wallet/remain"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/创建订单（套餐、单品）")
def applet_order_createOrder_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/createOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/计算订单总价")
def applet_order_calculateOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/下单前的预验证")
def applet_order_preValidOrderCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单匹配的优惠券")
def applet_order_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/选择座位")
def applet_order_take_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/释放座位")
def applet_order_cancle_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券数量")
def applet_coupon_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/coupon/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券列表")
def applet_coupon_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/coupon/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券详情")
def applet_coupon_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/coupon/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/根据优惠券查询学生可报名班级")
def applet_coupon_couponForClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/coupon/couponForClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/商品/课程套餐详情")
def applet_package_course_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/package/course/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/商品/课程单品详情")
def applet_goods_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/goods/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单优惠计算")
def applet_order_calculatePromotion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/applet/order/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页/校区详情")
def applet_schoolArea_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/schoolArea/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页/附近校区列表")
def applet_schoolArea_nearList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/schoolArea/nearList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页/优惠券可购买商品列表")
def applet_goods_forCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/goods/forCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页/banner详情")
def applet_banner_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/banner/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页/关于极客")
def applet_company_column_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/company/column/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/小程序码生成")
def applet_qr_getQr_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/qr/getQr"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/转介绍/用户转介绍金额")
def applet_finance_introduce_user_amount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/applet/finance/introduce/user/amount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/转介绍/领取至电子钱包")
def applet_finance_introduce_receive_receiveToWallet_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/applet/finance/introduce/receive/receiveToWallet"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/电子钱包/流水")
def applet_financial_wallet_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/applet/financial/wallet/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/转介绍/明细列表")
def applet_finance_introduce_receive_introduced_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/applet/finance/introduce/receive/introduced/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/转介绍/发放明细")
def applet_finance_introduce_receive_query_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/applet/finance/introduce/receive/query/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/学生可参加诊断列表")
def applet_diagnosis_usable_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/usable"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/获取试卷")
def applet_diagnosis_exam_paper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/exam/paper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/提交答案")
def applet_diagnosis_submit_exam_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/submit/exam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/诊断报告详情")
def applet_diagnosis_report_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/report/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/试题讲解")
def applet_diagnosis_question_analysis_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/question/analysis"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/查询学生的诊断报告")
def applet_diagnosis_report_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/report/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/诊断的成绩能报的班级")
def applet_diagnosis_able_class_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/able/class"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/是否应该去诊断")
def applet_diagnosis_should_diagnosis_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/should/diagnosis"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/入学诊断/学生是否可参加该诊断")
def applet_diagnosis_can_join_diagnosis_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/applet/diagnosis/can/join/diagnosis"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

