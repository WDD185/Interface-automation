
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("线上商店-通用接口/获取省市区")
def api_general_listAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/api/general/listAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-通用接口/获取校区")
def api_general_listSchoolAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/api/general/listSchoolAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-消息/消息列表")
def api_notice_listNotices_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/api/notice/listNotices"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-消息/消息聚合统计")
def api_notice_noticeStat_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/api/notice/noticeStat"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/添加埋点记录")
def api_eventLog_addEventLog_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/api/eventLog/addEventLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索回调")
def api_plaso_callback_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/api/plaso/callback"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

