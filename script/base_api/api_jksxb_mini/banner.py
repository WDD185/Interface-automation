
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("小程序/查询弹窗")
def banner_queryPopups_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/查询弹窗"
    url = f"/api-jksxb-mini/banner/queryPopups"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/弹窗已读")
def banner_readPopup_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/弹窗已读"
    url = f"/api-jksxb-mini/banner/readPopup"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/banner展示")
def banner_display_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/banner展示"
    url = f"/api-jksxb-mini/banner/display"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/点击记录")
def banner_click_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/点击记录"
    url = f"/api-jksxb-mini/banner/click"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

