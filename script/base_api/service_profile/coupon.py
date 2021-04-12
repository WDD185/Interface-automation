
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/前台业务/学生信息/发放新生优惠券")
def coupon_distributeAutoCouponByNewStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/前台业务/学生信息/发放新生优惠券"
    url = f"/service-profile/coupon/distributeAutoCouponByNewStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

