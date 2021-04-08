
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/作业/学生作业查阅情况详情")
def homework_readStatusOfStudentDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/readStatusOfStudentDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/草稿列表")
def homework_draft_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/draft"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/布置或保存草稿")
def homework_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/详情")
def homework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/查阅情况")
def homework_consultSituation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/consultSituation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/删除作业")
def homework_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/提醒学生查看作业")
def homework_remind_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/remind"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/已发布列表")
def homework_published_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/published"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/发布作业")
def homework_publishHomework_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/publishHomework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/作业列表")
def homework_homeworkList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/homeworkList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/班级列表")
def homework_myClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/myClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/学生作业查阅情况")
def homework_readStatusOfStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/readStatusOfStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/作业详情")
def homework_homeworkDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/homeworkDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/删除作业")
def homework_delHomework_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/delHomework"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通撤回作业")
def homework_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/homework/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

