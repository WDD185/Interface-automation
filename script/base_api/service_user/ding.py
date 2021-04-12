
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("员工手册/查看钉钉用户信息")
def ding_user_getUserInfo_v2_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "员工手册/查看钉钉用户信息"
    url = f"/service-user/ding/user/getUserInfo/v2"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

