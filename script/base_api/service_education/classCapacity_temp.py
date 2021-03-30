
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/教务管理/班级/查询预招人数限制")
def classCapacity_query_classLimit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classCapacity/query/classLimit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/查询满班目标")
def classCapacity_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classCapacity/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/新增满班目标")
def classCapacity_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classCapacity/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/修改满班目标")
def classCapacity_update_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classCapacity/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

