
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/基础/极师通用户登录")
def jst_app_auth_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/基础/极师通用户登录"
    url = f"/service-user/jst-app/auth"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/获取用户信息")
def jst_app_employees_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/首页/获取用户信息"
    url = f"/service-user/jst-app/employees/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

