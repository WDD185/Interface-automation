
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("教师基本功大赛/用户考试信息")
def basic_training_teacher_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/teacher_info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/倒计时")
def basic_training_countdown_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/countdown"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/获取考试信息")
def basic_training_exam_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/exam_info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/获取题目列表")
def basic_training_questions_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/questions"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/提交答案")
def basic_training_submit_answer_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/submit_answer"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/结果导出")
def basic_training_export_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/export"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/题目解析")
def basic_training_question_analysis_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/question_analysis"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/答题结果")
def basic_training_exam_result_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/exam_result"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/考试列表")
def basic_training_teacher_exams_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/basic_training/teacher_exams"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

