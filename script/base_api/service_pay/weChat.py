
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("引导微信网页授权")
def weChat_webPageOAuth_load_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "引导微信网页授权"
    url = f"/service-pay/weChat/webPageOAuth/load"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信网页授权")
def weChat_webPageOAuth_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "微信网页授权"
    url = f"/service-pay/weChat/webPageOAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

