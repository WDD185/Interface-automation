
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/人事管理/员工信息/查询部门员工")
def departments_departmentId_staffs_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/{departmentId}/staffs"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/查询子部门")
def departments_departmentId_children_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/{departmentId}/children"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/校区/获取全部大区校区")
def departments_schools_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/schools"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/部门详情")
def departments_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/创建部门")
def departments_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/修改部门")
def departments_departmentId_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/{departmentId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/校区/查询大区校区")
def departments_schools_queries_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/schools/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/删除部门")
def departments_departmentId_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/{departmentId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/查询所有部门")
def departments_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/部门设置/查询部门")
def departments_queries_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区管理/大区查询")
def departments_region_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/region/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区管理/列表查询")
def departments_school_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/school/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区管理/批量屏蔽校区")
def departments_school_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/school"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区管理/校区详情")
def departments_school_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/school/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区管理/批量连报")
def departments_school_communiqueRule_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/school/communiqueRule"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区管理/校区编辑")
def departments_school_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/departments/school"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

