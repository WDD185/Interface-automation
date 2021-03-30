
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("系统设置-订单设置-查询设置列表")
def ruleSetting_queryAll_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/ruleSetting/queryAll"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("系统设置-订单设置-编辑设置列表")
def ruleSetting_edit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/ruleSetting/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

