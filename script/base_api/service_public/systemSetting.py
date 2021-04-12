
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("小程序/首页/获取筛选项")
def systemSetting_getByType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/首页/获取筛选项"
    url = f"/service-public/systemSetting/getByType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

