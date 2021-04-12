
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/班主任/知识库/知识标签/新增")
def documentTag_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任/知识库/知识标签/新增"
    url = f"/service-crm/documentTag"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/修改")
def documentTag_put(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任/知识库/知识标签/修改"    
    url = f"/service-crm/documentTag"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/id查询")
def documentTag_id_get(id, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任/知识库/知识标签/id查询"
    url = f"/service-crm/documentTag/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/列表查询")
def documentTag_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任/知识库/知识标签/列表查询"
    url = f"/service-crm/documentTag/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/查询所有")
def documentTag_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任/知识库/知识标签/查询所有"
    url = f"/service-crm/documentTag/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/删除")
def documentTag_ids_delete(ids, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任/知识库/知识标签/删除"    
    url = f"/service-crm/documentTag/{ids}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

