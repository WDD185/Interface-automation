
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/招生目标设置/查询目标方案")
def targets_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/招生目标设置/设置默认目标方案")
def targets_setDef_targetId_patch(targetId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets/setDef/{targetId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/招生目标设置/删除目标方案")
def targets_targetId_delete(targetId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets/{targetId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/招生目标设置/查询目标方案详情")
def targets_targetId_get(targetId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets/{targetId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/招生目标设置/新增目标方案")
def targets_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/招生目标设置/修改目标方案")
def targets_targetId_patch(targetId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets/{targetId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/常规班班级年份期段")
def targets_getTerm_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets/getTerm"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/招生目标设置/编辑目标方案序列")
def targets_updateOrderNums_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/targets/updateOrderNums"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

