
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/批量转班/查询转班学生")
def classChange_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/查询转班学生"
    url = f"/service-profile/classChange/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/批量转班/查询转班费用课时")
def classChange_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/查询转班费用课时"
    url = f"/service-profile/classChange/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/批量转班/查询转班记录")
def classChange_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/查询转班记录"
    url = f"/service-profile/classChange/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/批量转班/批量转班")
def classChange_change_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/批量转班"
    url = f"/service-profile/classChange/change"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/转班/个人转班")
def classChange_query_class_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/转班/个人转班"
    url = f"/service-profile/classChange/query/class"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/批量转班/转班校验")
def classChange_validateChangeClassOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/转班校验"
    url = f"/service-profile/classChange/validateChangeClassOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

