
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/教务管理/入学诊断")
def entranceExam_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教务管理/入学诊断"
    url = f"/service-public/entranceExam/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/入学诊断/验证考试连接")
def entranceExam_valid_examUrl_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/入学诊断/验证考试连接"
    url = f"/service-public/entranceExam/valid/examUrl"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/入学诊断/开始考试")
def entranceExam_exam_begin_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/入学诊断/开始考试"
    url = f"/service-public/entranceExam/exam/begin"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/入学诊断/提交试卷")
def entranceExam_exam_end_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/入学诊断/提交试卷"
    url = f"/service-public/entranceExam/exam/end"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/入学诊断/获得密钥")
def entranceExam_secrect_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/入学诊断/获得密钥"
    url = f"/service-public/entranceExam/secrect"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

