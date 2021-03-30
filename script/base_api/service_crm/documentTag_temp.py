
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/班主任/知识库/知识标签/新增")
def documentTag_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/documentTag"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/修改")
def documentTag_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/documentTag"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/id查询")
def documentTag_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/documentTag/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/列表查询")
def documentTag_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/documentTag/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/查询所有")
def documentTag_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/documentTag/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识标签/删除")
def documentTag_ids_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/documentTag/{ids}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

