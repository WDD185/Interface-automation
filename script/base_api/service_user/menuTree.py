
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/人事管理/权限设置/权限列表")
def menuTree_employeeId_post(employeeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/menuTree/{employeeId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

