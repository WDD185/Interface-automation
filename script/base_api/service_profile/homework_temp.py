
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/作业/学生作业查阅情况详情")
def homework_readStatusOfStudentDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/readStatusOfStudentDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/草稿列表")
def homework_draft_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/draft"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/布置或保存草稿")
def homework_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/详情")
def homework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/查阅情况")
def homework_consultSituation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/consultSituation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/删除作业")
def homework_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/提醒学生查看作业")
def homework_remind_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/remind"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/已发布列表")
def homework_published_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/published"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/发布作业")
def homework_publishHomework_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/publishHomework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/作业列表")
def homework_homeworkList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/homeworkList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/班级列表")
def homework_myClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/myClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/学生作业查阅情况")
def homework_readStatusOfStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/readStatusOfStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/作业详情")
def homework_homeworkDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/homeworkDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/删除作业")
def homework_delHomework_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/delHomework"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通撤回作业")
def homework_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/homework/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/在线作业/查询题目")
def homework_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_research_web/homework/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/在线作业/新增题目")
def homework_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_research_web/homework/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/在线作业/删除题目")
def homework_del_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_research_web/homework/del"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通web/在线作业/查询题目")
def homework_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_teach_web/homework/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通web/在线作业/批改题目")
def homework_correct_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_teach_web/homework/correct"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/错题本/错题搜索列表")
def homework_searchWrongQuestions_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/homework/searchWrongQuestions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/错题本/错题详情")
def homework_getWrongQuestion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/homework/getWrongQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/错题本/删除错题本")
def homework_delWrongQuestion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/homework/delWrongQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮App/学习报告/错题列表")
def homework_getWrongQuestionList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/homework/getWrongQuestionList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮APP/错题本/错题列表默认帅选条件")
def homework_getDefaultCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/homework/getDefaultCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

