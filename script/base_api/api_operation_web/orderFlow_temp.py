
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/订单/计算订单总价")
def orderFlow_calculateOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/预占座位")
def orderFlow_preTake_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/preTake/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/释放座位")
def orderFlow_cancle_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/获取可使用优惠及优惠券")
def orderFlow_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/下单前的预验证")
def orderFlow_preValidOrderCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/计算促销活动价格")
def orderFlow_calculatePromotion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/客户管理/订单管理/订单/计算下段订单总价")
def orderFlow_calculateDownOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/calculateDownOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/客户管理/订单管理/订单/获取分段下可使用优惠及优惠券")
def orderFlow_queryDownMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/queryDownMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-占座位")
def orderFlow_take_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-取消占座")
def orderFlow_cancle_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-计算订单总价")
def orderFlow_calculateOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-下单前的预验证")
def orderFlow_preValidOrderCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-获取可使用优惠及优惠券")
def orderFlow_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/orderFlow/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/下单前的预验证")
def orderFlow_preValidOrderCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/orderFlow/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单优惠计算")
def orderFlow_calculatePromotion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/orderFlow/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单匹配的优惠券")
def orderFlow_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/orderFlow/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/计算订单总价")
def orderFlow_calculateOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/orderFlow/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/获取分段下可使用优惠及优惠券")
def orderFlow_queryDownMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/queryDownMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/计算分段下订单总价")
def orderFlow_calculateDownOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/orderFlow/calculateDownOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

