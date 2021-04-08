
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极教研/备课统计(教案)")
def teaching_plan_statistics_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/statistics/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/教案/审阅")
def teaching_plan_review_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/review"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/教案分享/点赞列表")
def teaching_plan_like_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/like/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/教案分享/教案点赞或取消点赞")
def teaching_plan_like_update_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/like/update"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/教案分享/教案阅读")
def teaching_plan_read_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/read"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的教案/教案撤回")
def teaching_plan_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的教案/教案详情查询")
def teaching_plan_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的教案/提交教案")
def teaching_plan_submit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/submit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的教案/当前教案")
def teaching_plan_current_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/teaching_plan/current/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

