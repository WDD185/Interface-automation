
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("新增或者修改权限")
def permission_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "新增或者修改权限"
    url = f"/service-user/permission"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("删除权限")
def permission_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "删除权限"    
    url = f"/service-user/permission"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

