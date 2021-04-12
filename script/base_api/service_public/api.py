
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("线上商店-消息/消息列表")
def api_notice_listNotices_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-消息/消息列表"
    url = f"/service-public/api/notice/listNotices"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-消息/消息聚合统计")
def api_notice_noticeStat_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-消息/消息聚合统计"
    url = f"/service-public/api/notice/noticeStat"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

