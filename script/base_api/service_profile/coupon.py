
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/前台业务/学生信息/发放新生优惠券")
def coupon_distributeAutoCouponByNewStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/coupon/distributeAutoCouponByNewStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

