
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("/通用/保存检查点数据")
def userCheckpoint_saveCheckpoint_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/通用/保存检查点数据"
    url = f"/service-profile/userCheckpoint/saveCheckpoint"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/通用/获取检查点数据")
def userCheckpoint_getCheckpoint_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/通用/获取检查点数据"
    url = f"/service-profile/userCheckpoint/getCheckpoint"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

