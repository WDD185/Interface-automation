
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/客户管理/报名/订单/新增订单")
def order_saveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/客户管理/报名/订单/新增订单"
    url = f"/api-operation-web/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/客户管理/报名/订单/查询单个订单")
def order_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/客户管理/报名/订单/查询单个订单"
    url = f"/api-operation-web/order/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/二维码查询订单")
def order_queryQrOrder_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/订单/二维码查询订单"
    url = f"/api-operation-web/order/queryQrOrder"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/查询订单列表")
def order_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/订单/查询订单列表"
    url = f"/api-operation-web/order/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/查询订单详情")
def order_queryOrderDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/订单/查询订单详情"
    url = f"/api-operation-web/order/queryOrderDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/取消订单")
def order_cancelOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/取消订单"
    url = f"/api-operation-web/order/cancelOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/修改收据")
def order_modifyFinancialFlow_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/修改收据"
    url = f"/api-operation-web/order/modifyFinancialFlow"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/修改备注")
def order_modifyRemark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/修改备注"
    url = f"/api-operation-web/order/modifyRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单作废")
def order_scrapOrder_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/订单作废"
    url = f"/api-operation-web/order/scrapOrder"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/客户管理/订单管理/订单/导出订单")
def order_export_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/客户管理/订单管理/订单/导出订单"
    url = f"/api-operation-web/order/export"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/客户管理/订单管理/订单/查询订单状态")
def order_queryStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/客户管理/订单管理/订单/查询订单状态"
    url = f"/api-operation-web/order/queryStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

