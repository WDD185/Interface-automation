
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("设置/消息/消息列表/自定义消息/用户接收")
def customMessageItem_get_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/customMessageItem/get"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/消息列表/自定义消息/用户阅读")
def customMessageItem_read_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/customMessageItem/read"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

