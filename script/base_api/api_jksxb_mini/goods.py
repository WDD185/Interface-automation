
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("线上商城/小程序/活动商品信息")
def goods_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商城/小程序/活动商品信息"
    url = f"/api-jksxb-mini/goods/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

