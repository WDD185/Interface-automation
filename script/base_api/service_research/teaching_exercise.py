
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极教研/刷题/点评")
def teaching_exercise_review_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/刷题/点评"
    url = f"/service-research/teaching_exercise/review"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的刷题/刷题撤回")
def teaching_exercise_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/我的刷题/刷题撤回"
    url = f"/service-research/teaching_exercise/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的刷题/刷题详情查询")
def teaching_exercise_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/我的刷题/刷题详情查询"
    url = f"/service-research/teaching_exercise/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的刷题/提交刷题")
def teaching_exercise_submit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/我的刷题/提交刷题"
    url = f"/service-research/teaching_exercise/submit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的刷题/当前刷题")
def teaching_exercise_current_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/我的刷题/当前刷题"
    url = f"/service-research/teaching_exercise/current/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课统计(刷题)")
def teaching_exercise_statistics_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/备课统计(刷题)"
    url = f"/service-research/teaching_exercise/statistics/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

