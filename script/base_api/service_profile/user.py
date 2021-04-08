
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码")
def user_studentId_backupMobilePhone_patch(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/user/{studentId}/backupMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码")
def user_studentId_bindingMobilePhone_patch(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/user/{studentId}/bindingMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录密码")
def user_type_signInPassword_patch(type, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/user/{type}/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

