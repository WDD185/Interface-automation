
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("JkyApp/登录")
def employee_login_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/登录"
    url = f"/api-operation-app/employee/login"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/登出")
def employee_logout_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/登出"
    url = f"/api-operation-app/employee/logout"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/员工信息")
def employee_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/员工信息"
    url = f"/api-operation-app/employee/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/获取短信验证码")
def employee_external_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/获取短信验证码"
    url = f"/api-operation-app/employee/external/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/校验手机验证码")
def employee_external_validity_verificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/校验手机验证码"
    url = f"/api-operation-app/employee/external/validity/verificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/修改员工密码")
def employee_signInPassword_patch(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/修改员工密码"
    url = f"/api-operation-app/employee/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询登录用户的授权校区")
def employee_schools_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/查询登录用户的授权校区"
    url = f"/api-operation-app/employee/schools"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询所有校区")
def employee_schools_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/查询所有校区"
    url = f"/api-operation-app/employee/schools/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询老师列表")
def employee_teacher_queries_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/查询老师列表"
    url = f"/api-operation-app/employee/teacher/queries"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询校区下的课程顾问")
def employee_schoolArea_course_consultant_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/查询校区下的课程顾问"
    url = f"/api-operation-app/employee/schoolArea/course-consultant"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询课程顾问并返回校区")
def employee_schoolArea_course_consultant_and_school_area_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/查询课程顾问并返回校区"
    url = f"/api-operation-app/employee/schoolArea/course-consultant-and-school-area"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

