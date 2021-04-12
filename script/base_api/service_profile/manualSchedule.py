
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/极客资料/手动发送开课前极客资料")
def manualSchedule_sendBeforeClassGeekMaterial_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/手动发送开课前极客资料"
    url = f"/service-profile/manualSchedule/sendBeforeClassGeekMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/预习数据/手动处理预习数据")
def manualSchedule_addPreviewData_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/预习数据/手动处理预习数据"
    url = f"/service-profile/manualSchedule/addPreviewData"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

