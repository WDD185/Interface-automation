
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("小程序/基础/用户登录（用户名密码）")
def wxMini_auth_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/基础/用户登录（用户名密码）"
    url = f"/service-user/wxMini/auth"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

