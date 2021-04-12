
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("小程序/商品/套餐检查服务")
def gos_api_package_check_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/商品/套餐检查服务"
    url = f"/service-gos/gos-api/package/check"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/商品/商品检查服务")
def gos_api_goods_check_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/商品/商品检查服务"
    url = f"/service-gos/gos-api/goods/check"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

