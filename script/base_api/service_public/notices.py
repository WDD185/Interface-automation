
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/消息通知/删除某则消息")
def notices_noticeId_delete(noticeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/{noticeId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/通知概况")
def notices_overviews_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/overviews"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/更新通知作业、发布内容详情")
def notices_noticeId_patch(noticeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/{noticeId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/作业、发布内容的阅读详情")
def notices_noticeId_reading_get(noticeId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/{noticeId}/reading"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/获取拒收规则")
def notices_reject_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/reject"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/拒收某类消息")
def notices_reject_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/reject"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/提醒学生阅读作业、发布内容")
def notices_noticeId_reminds_post(noticeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notices/{noticeId}/reminds"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

