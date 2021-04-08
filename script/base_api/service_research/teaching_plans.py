
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/章节目录/教案分享")
def teaching_plans_share_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plans/share/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/教案详情/讲次教案列表")
def teaching_plans_lecture_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plans/lecture/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审阅/教案列表")
def teaching_plans_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plans/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的教案/教案提交历史")
def teaching_plans_history_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plans/history/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

