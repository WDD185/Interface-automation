
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("备课评价/打分")
def courseWareScoreController_courseWareScore_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareScoreController/courseWareScore"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/根据课件查询评分")
def courseWareScoreController_queryScoreByContentId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareScoreController/queryScoreByContentId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/查询评分log")
def courseWareScoreController_queryScoreLogByContentId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareScoreController/queryScoreLogByContentId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/根据contentId和type查询评价")
def courseWareScoreController_queryEvaluateListById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareScoreController/queryEvaluateListById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("备课评价/根据contentId和type查询评分")
def courseWareScoreController_queryScoreById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/courseWareScoreController/queryScoreById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

