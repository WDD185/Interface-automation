
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/订单/单买订单列表")
def applet_order_orderListForSingle_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/orderListForSingle"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/单买下单")
def applet_order_saveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/创建订单（套餐、单品）")
def applet_order_createOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/createOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/计算订单总价")
def applet_order_calculateOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/下单前的预验证")
def applet_order_preValidOrderCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单匹配的优惠券")
def applet_order_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/选择座位")
def applet_order_take_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/释放座位")
def applet_order_cancle_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券数量")
def applet_coupon_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/coupon/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券列表")
def applet_coupon_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/coupon/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券详情")
def applet_coupon_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/coupon/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/根据优惠券查询学生可报名班级")
def applet_coupon_couponForClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/coupon/couponForClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单优惠计算")
def applet_order_calculatePromotion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/applet/order/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

