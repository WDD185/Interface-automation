
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/班主任管理/修改班主任")
def classDirector_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任管理/修改班主任"
    url = f"/service-education/classDirector/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("CRM/根据班主任查寻手下老师及班级")
def classDirector_getClassTeacherByDirector_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "CRM/根据班主任查寻手下老师及班级"
    url = f"/service-education/classDirector/getClassTeacherByDirector"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

