
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("伯索获取学生用户token")
def plaso_student_token_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/plaso/student/token"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索获取老师用户token")
def plaso_teacher_token_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/plaso/teacher/token"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("是否存在伯索学生身份")
def plaso_student_exist_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/plaso/student/exist"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("是否存在伯索老师身份")
def plaso_teacher_exist_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/plaso/teacher/exist"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

