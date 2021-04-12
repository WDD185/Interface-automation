
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("JkyAPP/保存沟通记录")
def lost_communicate_record_save_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/保存沟通记录"
    url = f"/api-operation-app/lost-communicate-record/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/按照学生获取-沟通记录")
def lost_communicate_record_get_records_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/按照学生获取-沟通记录"
    url = f"/api-operation-app/lost-communicate-record/get-records"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

