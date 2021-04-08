
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("CRM/学员管理/学员档案/家长信息")
def parent_baseInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/parent/baseInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("CRM/学员管理/学员档案/编辑家长信息")
def parent_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/parent/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

