
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/我的主页/优惠券数量")
def coupon_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-jksxb-mini/coupon/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券列表")
def coupon_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-jksxb-mini/coupon/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券详情")
def coupon_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-jksxb-mini/coupon/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

