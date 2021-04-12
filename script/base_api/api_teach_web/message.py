
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通/查询消息类型和对应的条数")
def message_inner_setting_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/查询消息类型和对应的条数"
    url = f"/api-teach-web/message/inner/setting/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/查询消息类型和对应的条数")
def message_inner_record_queryAll_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/查询消息类型和对应的条数"
    url = f"/api-teach-web/message/inner/record/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/消息设置为已读")
def message_inner_record_reading_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/消息设置为已读"
    url = f"/api-teach-web/message/inner/record/reading"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

