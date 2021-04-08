
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营APP订单查询")
def order_query_basic_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/query/basic"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP订单明细查询")
def order_query_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/query/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP修改订单备注")
def order_modifyRemark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/modifyRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP修改订单状态")
def order_update_status_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/update/status"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP订单预校验")
def order_preValidOrderCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP订单获取优惠信息")
def order_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP订单计算订单价格")
def order_calculateOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP保存订单")
def order_saveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP占座")
def order_getOccupiedSeatOrOccupy_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/getOccupiedSeatOrOccupy"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营app作废订单")
def order_scrapOrder_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/scrapOrder"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营app取消订单")
def order_cancelOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/order/cancelOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

