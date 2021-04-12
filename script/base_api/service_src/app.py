
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("资源中心/获取签名")
def app_getSignature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "资源中心/获取签名"
    url = f"/service-src/app/getSignature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/获取视频签名")
def app_getVodSignature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "资源中心/获取视频签名"
    url = f"/service-src/app/getVodSignature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/获取cos签名")
def app_getPutSignature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "资源中心/获取cos签名"
    url = f"/service-src/app/getPutSignature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

