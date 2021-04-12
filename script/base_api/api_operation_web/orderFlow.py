
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/客户管理/订单管理/订单/计算下段订单总价")
def orderFlow_calculateDownOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/客户管理/订单管理/订单/计算下段订单总价"
    url = f"/api-operation-web/orderFlow/calculateDownOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/客户管理/订单管理/订单/获取分段下可使用优惠及优惠券")
def orderFlow_queryDownMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/客户管理/订单管理/订单/获取分段下可使用优惠及优惠券"
    url = f"/api-operation-web/orderFlow/queryDownMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-占座位")
def orderFlow_take_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "客户管理-报名-订单-占座位"
    url = f"/api-operation-web/orderFlow/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-取消占座")
def orderFlow_cancle_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "客户管理-报名-订单-取消占座"
    url = f"/api-operation-web/orderFlow/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-计算订单总价")
def orderFlow_calculateOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "客户管理-报名-订单-计算订单总价"
    url = f"/api-operation-web/orderFlow/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-下单前的预验证")
def orderFlow_preValidOrderCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "客户管理-报名-订单-下单前的预验证"
    url = f"/api-operation-web/orderFlow/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("客户管理-报名-订单-获取可使用优惠及优惠券")
def orderFlow_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "客户管理-报名-订单-获取可使用优惠及优惠券"
    url = f"/api-operation-web/orderFlow/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

