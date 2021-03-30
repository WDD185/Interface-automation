
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/班主任/知识库/知识/新增")
def document_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/修改")
def document_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/id查询")
def document_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/列表查询")
def document_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/上传文件")
def document_uploadFile_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document/uploadFile"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/浏览量")
def document_addViewCount_id_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document/addViewCount/{id}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/删除")
def document_ids_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document/{ids}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任/知识库/知识/浏览量")
def document_addViewCount_id_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/document/addViewCount/{id}"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

