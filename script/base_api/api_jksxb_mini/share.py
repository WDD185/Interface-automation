
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("小程序预生成分享ID")
def share_preCreateShareIds_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序预生成分享ID"
    url = f"/api-jksxb-mini/share/preCreateShareIds"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序保存分享")
def share_saveShare_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序保存分享"
    url = f"/api-jksxb-mini/share/saveShare"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序获取分享明细")
def share_getShareDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序获取分享明细"
    url = f"/api-jksxb-mini/share/getShareDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序获取分享明细")
def share_getShareDetailAndRecordBrowse_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序获取分享明细"
    url = f"/api-jksxb-mini/share/getShareDetailAndRecordBrowse"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

