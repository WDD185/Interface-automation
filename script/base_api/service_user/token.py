
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/校验token")
def token_valid_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/校验token"
    url = f"/service-user/token/valid"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

