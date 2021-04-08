
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("员工手册/列表查询")
def regime_listRegimes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/listRegimes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/内容查询")
def regime_listRegimeContents_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/listRegimeContents"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/书架")
def regime_listRegimeOnReadNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/listRegimeOnReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/埋点记录/每页时长")
def regime_log_content_duration_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/log/content/duration"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/埋点记录/缩略图跳转")
def regime_log_thumbnail_from_to_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/log/thumbnail/from/to"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/埋点记录/发送通知")
def regime_log_send_notice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/log/send/notice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/埋点记录/通知进入")
def regime_log_visit_from_notice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/log/visit/from/notice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/埋点记录/访问页面")
def regime_log_visit_content_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/log/visit/content"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("员工手册/埋点记录/关闭页面")
def regime_log_leave_content_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-periodical/regime/log/leave/content"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

