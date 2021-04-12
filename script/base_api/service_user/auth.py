
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/基础/用户登录")
def auth_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/基础/用户登录"
    url = f"/service-user/auth"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/基础/用户登录")
def auth_employee_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/基础/用户登录"
    url = f"/service-user/auth/employee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/基础/用户登录")
def auth_dingQR_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/基础/用户登录"
    url = f"/service-user/auth/dingQR"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

