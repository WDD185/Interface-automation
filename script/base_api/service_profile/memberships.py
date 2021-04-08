
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/花名册/查询学生续报状态")
def memberships_students_continueStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/students/continueStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/查询老师所有学生")
def memberships_overview_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/overview"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/导出班级花名册")
def memberships_classes_export_classId_get(classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/classes/export/{classId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/查询班级花名册")
def memberships_classes_classId_get(classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/classes/{classId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/点名/查询本堂课实际上课学生")
def memberships_schedules_classScheduleId_get(classScheduleId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/schedules/{classScheduleId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/查询学生就读历史")
def memberships_studentId_history_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/{studentId}/history"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/查询学生的在读班级信息")
def memberships_student_currentClass_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/student/currentClass"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/导出/导出花名册")
def memberships_classes_exportClassStudentInfo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/classes/exportClassStudentInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/查询班级花名册")
def memberships_classes_queryClassStudentInfo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/memberships/classes/queryClassStudentInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

