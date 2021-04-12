
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("设置/消息/消息列表/系统消息/编辑")
def systemMessage_edit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "设置/消息/消息列表/系统消息/编辑"
    url = f"/service-crm/systemMessage/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/消息列表/系统消息/修改状态")
def systemMessage_updateStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "设置/消息/消息列表/系统消息/修改状态"
    url = f"/service-crm/systemMessage/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/消息列表/系统消息/查询列表")
def systemMessage_queryAll_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "设置/消息/消息列表/系统消息/查询列表"
    url = f"/service-crm/systemMessage/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/消息列表/系统消息/查看单个")
def systemMessage_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "设置/消息/消息列表/系统消息/查看单个"
    url = f"/service-crm/systemMessage/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

