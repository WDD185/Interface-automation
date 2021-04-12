
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/App资源/获取热更新资源two")
def version_platform_platform_available_get(platform, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/App资源/获取热更新资源two"
    url = f"/service-public/version/{platform}/platform/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

