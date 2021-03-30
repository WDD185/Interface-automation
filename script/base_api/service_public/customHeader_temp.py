
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/通用/用户自定义列查询")
def customHeader_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/customHeader/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/通用/用户自定义列新增")
def customHeader_save_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/customHeader/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

