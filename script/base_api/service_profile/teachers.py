
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通/老师信息/老师班级（新）")
def teachers_classes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/老师信息/老师班级（新）"
    url = f"/service-profile/teachers/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页/查询上月老师教学情况")
def teachers_teacherId_teach_situation_get(teacherId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/首页/查询上月老师教学情况"
    url = f"/service-profile/teachers/{teacherId}/teach-situation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页/查询老师某个时间段排课计划")
def teachers_teacherId_timetables_queries_get(teacherId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/首页/查询老师某个时间段排课计划"
    url = f"/service-profile/teachers/{teacherId}/timetables/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/课表/查询老师在目前所教的班级")
def teachers_teacherId_classes_get(teacherId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/课表/查询老师在目前所教的班级"
    url = f"/service-profile/teachers/{teacherId}/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页/班级列表")
def teachers_classes_contidion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/首页/班级列表"
    url = f"/service-profile/teachers/classes/contidion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

