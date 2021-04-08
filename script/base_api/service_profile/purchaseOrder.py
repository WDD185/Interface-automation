
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中课程总数")
def purchaseOrder_studentId_student_count_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/purchaseOrder/{studentId}/student/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/删除某个学生购课单中的某一条记录")
def purchaseOrder_purchaseId_studentstudentId_delete(purchaseId, studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/purchaseOrder/{purchaseId}/student{studentId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/某个学生向购课单中添加课程")
def purchaseOrder_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量删除某个学生购课单中的多条记录")
def purchaseOrder_studentId_student_delete(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中的课程")
def purchaseOrder_studentId_student_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量修改某个学生购课单中多条记录的状态")
def purchaseOrder_studentId_student_put(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):    
    url = host + f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/修改某个学生购课单中某一条记录的状态")
def purchaseOrder_purchaseId_student_studentId_patch(purchaseId, studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/purchaseOrder/{purchaseId}/student/{studentId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

