
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("题库来源优化/根据标签获取筛选分类列表")
def question_source_category_get(category, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库来源优化/根据标签获取筛选分类列表"
    url = f"/service-question/question_source/{category}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库来源优化/省市区联动数据获取")
def question_source_city_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库来源优化/省市区联动数据获取"
    url = f"/service-question/question_source/city"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库来源优化/大区区域校区联动数据获取")
def question_source_region_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库来源优化/大区区域校区联动数据获取"
    url = f"/service-question/question_source/region"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库来源优化/杯赛筛选数据获取")
def question_source_match_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库来源优化/杯赛筛选数据获取"
    url = f"/service-question/question_source/match"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库来源优化/课程班型筛选数据获取")
def question_source_course_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库来源优化/课程班型筛选数据获取"
    url = f"/service-question/question_source/course"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库来源优化/学校筛选功能")
def question_source_school_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库来源优化/学校筛选功能"
    url = f"/service-question/question_source/school"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题目排重/移入撤回标签")
def question_source_duplicate_handle_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题目排重/移入撤回标签"
    url = f"/service-question/question_source/duplicate_handle"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/返回所有区域结果集")
def question_source_getAllArea_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极题库/返回所有区域结果集"
    url = f"/service-question/question_source/getAllArea"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

