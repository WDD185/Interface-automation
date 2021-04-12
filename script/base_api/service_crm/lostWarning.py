
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/CRM/流失管理/预流失学员/预流失学员列表查询")
def lostWarning_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/流失管理/预流失学员/预流失学员列表查询"
    url = f"/service-crm/lostWarning/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/流失管理/预流失学员/预流失学员导出")
def lostWarning_export_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/流失管理/预流失学员/预流失学员导出"
    url = f"/service-crm/lostWarning/export"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/流失管理/预流失学员/编辑预流失原因")
def lostWarning_editReason_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/流失管理/预流失学员/编辑预流失原因"
    url = f"/service-crm/lostWarning/editReason"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/流失管理/预流失学员/查询预流失原因")
def lostWarning_getPreLostReason_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/流失管理/预流失学员/查询预流失原因"
    url = f"/service-crm/lostWarning/getPreLostReason"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/流失管理/预流失学员/获取班主任和教师")
def lostWarning_getTeachersAndDirectors_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/流失管理/预流失学员/获取班主任和教师"
    url = f"/service-crm/lostWarning/getTeachersAndDirectors"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

