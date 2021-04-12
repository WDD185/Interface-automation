
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极数据/查询期段下拉列表")
def teacherValueRank_term_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极数据/查询期段下拉列表"
    url = f"/service-statistics-metrics/teacherValueRank/term"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询C值排名列表")
def teacherValueRank_cValueRank_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极数据/查询C值排名列表"
    url = f"/service-statistics-metrics/teacherValueRank/cValueRank"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询C值班级详情")
def teacherValueRank_classDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极数据/查询C值班级详情"
    url = f"/service-statistics-metrics/teacherValueRank/classDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询C值含低价班班级详情")
def teacherValueRank_lowPriceClassDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极数据/查询C值含低价班班级详情"
    url = f"/service-statistics-metrics/teacherValueRank/lowPriceClassDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

