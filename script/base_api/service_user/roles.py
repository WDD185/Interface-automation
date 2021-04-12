
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/人事管理/权限设置/角色列表")
def roles_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/角色列表"
    url = f"/service-user/roles"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/用户授权/查看此角色下的用户列表")
def roles_roleId_users_get(roleId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/用户授权/查看此角色下的用户列表"
    url = f"/service-user/roles/{roleId}/users"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/查看角色下的权限组")
def roles_roleId_get(roleId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/查看角色下的权限组"
    url = f"/service-user/roles/{roleId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/删除角色")
def roles_roleId_delete(roleId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/删除角色"    
    url = f"/service-user/roles/{roleId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/用户授权/员工添加角色")
def roles_roleId_employees_post(roleId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/用户授权/员工添加角色"
    url = f"/service-user/roles/{roleId}/employees"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/新增角色")
def roles_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/新增角色"
    url = f"/service-user/roles"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/用户授权/从角色中删掉某人")
def roles_roleId_users_userId_delete(roleId, userId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/用户授权/从角色中删掉某人"    
    url = f"/service-user/roles/{roleId}/users/{userId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/权限设置/修改角色")
def roles_roleId_patch(roleId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/权限设置/修改角色"
    url = f"/service-user/roles/{roleId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

