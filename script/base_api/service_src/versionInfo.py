
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("代码版本接口")
def versionInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "代码版本接口"
    url = f"/service-src/versionInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

