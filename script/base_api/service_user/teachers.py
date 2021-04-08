
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/修改自己助教的密码")
def teachers_setPwForAssistant_patch(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/teachers/setPwForAssistant"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/教师授权/修改老师信息")
def teachers_teacherId_post(teacherId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/teachers/{teacherId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/教师授权/查询老师")
def teachers_queries_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/teachers/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

