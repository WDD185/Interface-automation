
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极题库/章节树/章节树查询")
def chapter_tree_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/chapter_tree/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/章节树/教材版本和学期查询")
def chapter_tree_version_semester_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/chapter_tree/version_semester/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/章节树/章节树保存")
def chapter_tree_save_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/chapter_tree/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

