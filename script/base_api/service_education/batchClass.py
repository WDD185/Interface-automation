
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/教务管理/班级/批量建班/上传excel并添加班级")
def batchClass_createClass_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教务管理/班级/批量建班/上传excel并添加班级"
    url = f"/service-education/batchClass/createClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/班级/批量建班/下载模板")
def batchClass_downModel_class_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教务管理/班级/批量建班/下载模板"
    url = f"/service-education/batchClass/downModel/class"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

