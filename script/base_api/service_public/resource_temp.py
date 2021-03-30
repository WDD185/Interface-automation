
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/App资源/批量删除热更新资源")
def resource_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/resource"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/App资源/批量修改热更新资源状态")
def resource_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/resource"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/App资源/新增一个热更新资源")
def resource_platform_platform_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/resource/{platform}/platform"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/App资源/获取热更新资源One")
def resource_platform_platform_available_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/resource/{platform}/platform/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

