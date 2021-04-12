
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("部门/获取部门树")
def department_getDepartmentTree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "部门/获取部门树"
    url = f"/api-admin/department/getDepartmentTree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("部门/查询部门树")
def department_searchDepartmentTree_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "部门/查询部门树"
    url = f"/api-admin/department/searchDepartmentTree"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("部门/维护组织类型")
def department_updateDepartBusiType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "部门/维护组织类型"
    url = f"/api-admin/department/updateDepartBusiType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("部门/获取校区下拉框")
def department_getSchoolCode_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "部门/获取校区下拉框"
    url = f"/api-admin/department/getSchoolCode"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("部门/获取校区树")
def department_getSchoolTree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "部门/获取校区树"
    url = f"/api-admin/department/getSchoolTree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

