
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/极数据神策登录/获取code")
def sa_getCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/sa/getCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据神策登录/登录")
def sa_login_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/sa/login"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据神策登录/验证code")
def sa_token_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/sa/token"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据神策登录/获取user")
def sa_user_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/sa/user"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

