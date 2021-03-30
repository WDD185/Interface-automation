
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("伯索获取学生用户token")
def plaso_student_token_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/plaso/student/token"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索获取老师用户token")
def plaso_teacher_token_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/plaso/teacher/token"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索账密鉴权")
def plaso_auth_employee_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/plaso/auth/employee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索钉钉扫码鉴权")
def plaso_auth_dingQR_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/plaso/auth/dingQR"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("是否存在伯索学生身份")
def plaso_student_exist_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/plaso/student/exist"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("是否存在伯索老师身份")
def plaso_teacher_exist_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/plaso/teacher/exist"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

