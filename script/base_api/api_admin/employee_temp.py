
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("JkyApp/登录")
def employee_login_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/login"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/登出")
def employee_logout_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/logout"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/员工信息")
def employee_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/获取短信验证码")
def employee_external_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/external/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/校验手机验证码")
def employee_external_validity_verificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/external/validity/verificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/修改员工密码")
def employee_signInPassword_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询登录用户的授权校区")
def employee_schools_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/schools"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询所有校区")
def employee_schools_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/schools/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询老师列表")
def employee_teacher_queries_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/teacher/queries"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询校区下的课程顾问")
def employee_schoolArea_course_consultant_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/schoolArea/course-consultant"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询课程顾问并返回校区")
def employee_schoolArea_course_consultant_and_school_area_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/employee/schoolArea/course-consultant-and-school-area"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/组织员工列表")
def employee_getEmployeeShowList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/getEmployeeShowList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/异动员工列表")
def employee_getChangeEmployeeShowList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/getChangeEmployeeShowList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/新增员工")
def employee_insertEmployee_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/insertEmployee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/停用员工帐号")
def employee_disableEmployee_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/disableEmployee"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/删除员工")
def employee_deleteEmployee_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/deleteEmployee"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/标记为已处理")
def employee_markHandledChangeEmployee_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/markHandledChangeEmployee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/设置可操作校区")
def employee_setOperableSchool_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/setOperableSchool"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/设置授课校区")
def employee_setTeachableSchool_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/setTeachableSchool"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/设置授课学段")
def employee_setTeachDegree_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/setTeachDegree"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/设置授课科目")
def employee_setTeachSubject_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/setTeachSubject"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/获取员工概览信息")
def employee_getEmployeeDetailOutDto_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/getEmployeeDetailOutDto"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/获取授课学段下拉框")
def employee_getTeachDegree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/getTeachDegree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/获取授课科目下拉框")
def employee_getTeachSubject_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/employee/getTeachSubject"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

