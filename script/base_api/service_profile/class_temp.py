
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表的筛选条件")
def class_selection_elective_Courses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/selection/elective/Courses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/刷新班级缓存")
def class_refreshCache_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/refreshCache"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表")
def class_studentId_student_allowable_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/{studentId}/student/allowable"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班级推送/班级的推送详情")
def class_classId_purchasesDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/{classId}/purchasesDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/刷新校区缓存")
def class_refreshSchoolIdCache_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/refreshSchoolIdCache"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取同大区下的所有校区")
def class_schoolAreaId_getSameLevelSchoolArea_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/{schoolAreaId}/getSameLevelSchoolArea"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的某一个班级的详细信息")
def class_classId_alternative_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/class/{classId}/alternative/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

