
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("JkyApp/查询班级列表")
def classes_queryList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/查询班级列表"
    url = f"/api-operation-app/classes/queryList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询班级座位列表")
def classes_seats_queryByClassId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/查询班级座位列表"
    url = f"/api-operation-app/classes/seats/queryByClassId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询订单班级列表")
def classes_order_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/查询订单班级列表"
    url = f"/api-operation-app/classes/order/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP订单查询班级")
def classes_order_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营APP订单查询班级"
    url = f"/api-operation-app/classes/order/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

