
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮App/错题本/错题搜索列表")
def homework_searchWrongQuestions_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮App/错题本/错题搜索列表"
    url = f"/api-jksxb-app/homework/searchWrongQuestions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/错题本/错题详情")
def homework_getWrongQuestion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮App/错题本/错题详情"
    url = f"/api-jksxb-app/homework/getWrongQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/错题本/删除错题本")
def homework_delWrongQuestion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮App/错题本/删除错题本"
    url = f"/api-jksxb-app/homework/delWrongQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/学习报告/错题列表")
def homework_getWrongQuestionList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮App/学习报告/错题列表"
    url = f"/api-jksxb-app/homework/getWrongQuestionList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮APP/错题本/错题列表默认帅选条件")
def homework_getDefaultCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮APP/错题本/错题列表默认帅选条件"
    url = f"/api-jksxb-app/homework/getDefaultCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

