
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极数据/查询期段下拉列表")
def teacherValueRank_term_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/teacherValueRank/term"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询C值排名列表")
def teacherValueRank_cValueRank_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/teacherValueRank/cValueRank"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询C值班级详情")
def teacherValueRank_classDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/teacherValueRank/classDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

