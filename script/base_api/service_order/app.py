
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/订单/计算订单总价(旧)")
def app_order_countOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/countOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/app端获取可使用优惠及优惠券")
def app_order_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/计算订单总价")
def app_order_calculateOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/新增订单")
def app_order_saveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/订单")
def app_order_queryOrderGeneralForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/queryOrderGeneralForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/订单/查询订单详情")
def app_order_queryOrderDetailForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/queryOrderDetailForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券/根据优惠券查询学生可报名班级")
def app_coupon_couponForAppClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/coupon/couponForAppClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/报名/app端下单前的预验证")
def app_order_preValidOrderCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/查询订单状态")
def app_order_queryStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/queryStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/释放座位")
def app_order_cancle_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/验证学生重复生成订单")
def app_order_studentHasOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/studentHasOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单1/查询订单状态1")
def app_order_queryTest_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/queryTest"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/预占座位")
def app_order_take_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/报名/获取可使用优惠")
def app_order_discounts_queryMatchDiscount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/discounts/queryMatchDiscount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/订单状态修改")
def app_order_updateStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/新增订单(旧)")
def app_order_save_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/查询订单")
def app_order_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/二维码查询订单")
def app_order_qr_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/qr/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券张数")
def app_coupon_countValidCouponItemByStudentIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/coupon/countValidCouponItemByStudentIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券/优惠券列表")
def app_coupon_selectCouponItemsByStudentIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/coupon/selectCouponItemsByStudentIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券/优惠券详情")
def app_coupon_selectCouponItemByIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/coupon/selectCouponItemByIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/获取可使用优惠券")
def app_coupon_queryMatchCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/coupon/queryMatchCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/计算促销活动价格")
def app_order_calculatePromotion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/app/order/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

