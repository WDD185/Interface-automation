
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/查询题目列表")
def question_jst_questions_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/题目详情查询")
def question_jst_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/提交纠错")
def question_jst_rectify_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/rectify"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人提报纠错题目列表")
def question_jst_question_rectify_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/question_rectify"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人收藏题目列表")
def question_jst_personal_bookmark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/personal_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/收藏、移除收藏")
def question_jst_question_bookmark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/question_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/新建收藏夹")
def question_jst_bookmark_create_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/bookmark_create"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/删除收藏夹")
def question_jst_bookmark_delete_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/bookmark_delete"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/修改收藏夹")
def question_jst_bookmark_update_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/bookmark_update"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/移动收藏夹")
def question_jst_bookmark_move_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/bookmark_move"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人收藏夹目录列表")
def question_jst_bookmark_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/bookmark_list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/题目下载")
def question_jst_download_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/download"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/删除纠错")
def question_jst_rectify_delete_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_jst/rectify_delete"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

