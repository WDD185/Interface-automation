
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/删除用户设备绑定关系")
def pushRelationship_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/pushRelationship"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/新增用户设备绑定关系")
def pushRelationship_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/pushRelationship"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

