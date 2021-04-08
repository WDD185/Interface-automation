
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/班主任/知识库/知识分类/新增")
def documentDirectory_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识分类/修改")
def documentDirectory_put(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):    
    url = host + f"/service-crm/documentDirectory"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识分类/id查询")
def documentDirectory_id_get(id, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识分类/列表查询")
def documentDirectory_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识分类/查询所有")
def documentDirectory_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识分类/删除")
def documentDirectory_ids_delete(ids, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory/{ids}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("知识/知识列表/列表树查询")
def documentDirectory_queryChildDirectory_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory/queryChildDirectory"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("知识/知识列表/目录树查询")
def documentDirectory_queryDirectoryTree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-crm/documentDirectory/queryDirectoryTree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

