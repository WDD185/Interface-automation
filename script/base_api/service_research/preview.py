
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极教研/课件库/预习题目添加")
def preview_add_questions_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/课件库/预习题目添加"
    url = f"/service-research/preview/add/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/课件库/预习题目取消")
def preview_less_questions_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/课件库/预习题目取消"
    url = f"/service-research/preview/less/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/课件库/查询预习题目列表")
def preview_query_questions_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/课件库/查询预习题目列表"
    url = f"/service-research/preview/query/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

