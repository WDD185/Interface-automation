
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("设置/消息/我的消息/查询列表")
def systemMessageItem_queryAll_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/systemMessageItem/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/我的消息/删除")
def systemMessageItem_del_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/systemMessageItem/del"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/我的消息/标记为已读")
def systemMessageItem_markRead_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/systemMessageItem/markRead"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/我的消息/系统消息/用户接收")
def systemMessageItem_get_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/systemMessageItem/get"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

