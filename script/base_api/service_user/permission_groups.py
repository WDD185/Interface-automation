
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/人事管理/权限设置/修改权限组")
def permission_groups_groupId_patch(groupId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/修改权限组"
    url = f"/service-user/permission-groups/{groupId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/删除权限组")
def permission_groups_id_delete(id, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/删除权限组"    
    url = f"/service-user/permission-groups/{id}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/新增权限组")
def permission_groups_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/新增权限组"
    url = f"/service-user/permission-groups"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/查看权限组下的详细权限")
def permission_groups_groupId_get(groupId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/查看权限组下的详细权限"
    url = f"/service-user/permission-groups/{groupId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/权限组列表")
def permission_groups_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/权限组列表"
    url = f"/service-user/permission-groups"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

