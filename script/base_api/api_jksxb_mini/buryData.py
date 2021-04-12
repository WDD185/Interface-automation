
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("线上商城/小程序/埋点")
def buryData_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商城/小程序/埋点"
    url = f"/api-jksxb-mini/buryData/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

