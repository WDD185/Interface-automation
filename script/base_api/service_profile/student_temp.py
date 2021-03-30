
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/获取学生所有班级")
def student_class_getAllClass_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/class/getAllClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生基本信息")
def student_studentId_basicInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/{studentId}/basicInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改当前学生用户一个或多个基础属性值")
def student_studentId_attribute_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/{studentId}/attribute"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/学生信息/查询学生明细")
def student_class_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/class/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/某个学生用户主动发起调课请求")
def student_studentId_transferringClass_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/{studentId}/transferringClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生电子账户")
def student_studentId_electronicAccount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/{studentId}/electronicAccount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生的续报类型")
def student_studentId_signUpType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/{studentId}/signUpType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/学生信息/获取潜在学生基本信息")
def student_potential_items_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/potential/items"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/学生信息/获取在读学生基本信息")
def student_reading_items_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/reading/items"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/判断学生将要报名的课程和已经报名的课程是否有排课冲突")
def student_studentId_class_classId_Conflict_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/{studentId}/class/{classId}/Conflict"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/学生信息/获取已结业学生基本信息")
def student_completed_items_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/completed/items"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/学生信息/获取学生基本信息")
def student_all_items_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/all/items"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任机制/学员管理/学生内页/查询学生考试记录--成长轨迹")
def student_administration_exam_student_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/administration/exam/student/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任机制/学员管理/学生内页/根据学生ID查询学生页标签信息")
def student_administration_labels_student_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/administration/labels/student/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任机制/学员管理/查询学员明细")
def student_administration_classes_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/student/administration/classes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

