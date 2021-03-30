
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/备课/备课教材查询")
def prepareLessons_prepareTextbook_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/prepareLessons/prepareTextbook"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课/备课教材可关联班级")
def prepareLessons_textbook_classes_available_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/prepareLessons/textbook/classes/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课/新增备课教材")
def prepareLessons_prepareTextbook_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/prepareLessons/prepareTextbook"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课/删除备课教材")
def prepareLessons_prepareTextbook_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/prepareLessons/prepareTextbook"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课/教材/查询班级是否关联了教材")
def prepareLessons_related_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/prepareLessons/related"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课/教师可用教材查询")
def prepareLessons_textbook_available_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/prepareLessons/textbook/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

