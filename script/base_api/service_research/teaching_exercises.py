
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极教研/刷题详情/讲次刷题列表")
def teaching_exercises_lecture_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/刷题详情/讲次刷题列表"
    url = f"/service-research/teaching_exercises/lecture/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审阅/刷题列表")
def teaching_exercises_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/备课审阅/刷题列表"
    url = f"/service-research/teaching_exercises/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的刷题/刷题提交历史")
def teaching_exercises_history_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/我的刷题/刷题提交历史"
    url = f"/service-research/teaching_exercises/history/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

