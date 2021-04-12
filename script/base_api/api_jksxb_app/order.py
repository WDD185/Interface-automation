
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/订单/新增订单")
def order_saveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/订单/新增订单"
    url = f"/api-jksxb-app/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/我的订单列表")
def order_myOrder_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/订单/我的订单列表"
    url = f"/api-jksxb-app/order/myOrder"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/查询订单详情")
def order_myOrderDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/订单/查询订单详情"
    url = f"/api-jksxb-app/order/myOrderDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/删除订单")
def order_deleteOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/订单/删除订单"
    url = f"/api-jksxb-app/order/deleteOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/取消订单")
def order_cancelOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/订单/取消订单"
    url = f"/api-jksxb-app/order/cancelOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/查询订单状态")
def order_queryStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/订单/查询订单状态"
    url = f"/api-jksxb-app/order/queryStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

