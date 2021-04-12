
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("JkyAPP/双师播放地址")
def videoPlayAddress_create_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/双师播放地址"
    url = f"/service-profile/videoPlayAddress/create"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/双师播放地址")
def videoPlayAddress_queryEntity_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/双师播放地址"
    url = f"/service-profile/videoPlayAddress/queryEntity"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

