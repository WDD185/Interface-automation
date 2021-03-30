
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("备课评价/新增评价")
def courseWareEvaluateController_addEvaluate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareEvaluateController/addEvaluate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/根据课件查询评价")
def courseWareEvaluateController_queryEvaluateList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareEvaluateController/queryEvaluateList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/评价列表")
def courseWareEvaluateController_queryEvaluateByParam_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareEvaluateController/queryEvaluateByParam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/查询评价详情")
def courseWareEvaluateController_queryEvaluateById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareEvaluateController/queryEvaluateById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/删除评价")
def courseWareEvaluateController_deleteEvaluate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareEvaluateController/deleteEvaluate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/查询评价列表")
def courseWareEvaluateController_queryEvaluateListById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareEvaluateController/queryEvaluateListById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

