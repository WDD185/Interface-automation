
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("新增或者修改权限")
def permission_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/permission"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("删除权限")
def permission_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/permission"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/添加权限")
def permission_addPermission_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/addPermission"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/修改权限")
def permission_updatePermission_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/updatePermission"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/删除权限")
def permission_deletePermission_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/deletePermission"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/删除多个权限")
def permission_deletePermissions_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/deletePermissions"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询所有平台")
def permission_queryAllPlatform_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryAllPlatform"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询员工授权的所有平台")
def permission_queryAllPlatformByEmployeeId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryAllPlatformByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询员工授权的所有PC平台")
def permission_queryAllPCPlatformByEmployeeId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryAllPCPlatformByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询整颗权限树，从根开始")
def permission_queryPermissionTree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryPermissionTree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询某个平台下的权限树")
def permission_queryPermissionTreeByPlatform_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryPermissionTreeByPlatform"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询员工对应的URL权限")
def permission_queryPermissionUrlByEmployeeId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryPermissionUrlByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/根据员工ID查询员工的权限")
def permission_queryPermissionsByEmployeeId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryPermissionsByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询员工对应的权限树")
def permission_queryPermissionTreeByEmployeeId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryPermissionTreeByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/修改角色与权限绑定关系")
def permission_updateRolePermission_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/updateRolePermission"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/根据角色ID查询角色的权限")
def permission_queryPermissionsByRoleId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryPermissionsByRoleId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/查询角色授权的所有平台")
def permission_queryAllPlatformByRoleId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/queryAllPlatformByRoleId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极权限/根据角色ID查询角色的权限--已选择的标出")
def permission_querySelectPermissionTreeByRoleId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_admin/permission/querySelectPermissionTreeByRoleId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

