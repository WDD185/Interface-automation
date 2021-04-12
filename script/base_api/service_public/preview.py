
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/ppt用户/新增用户")
def preview_ppt_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/ppt用户/新增用户"
    url = f"/service-public/preview/ppt/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/ppt用户/查询用户")
def preview_ppt_get_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/ppt用户/查询用户"
    url = f"/service-public/preview/ppt/get"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

