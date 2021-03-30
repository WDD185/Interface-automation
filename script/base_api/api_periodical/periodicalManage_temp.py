
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("管理内刊/管理端/发送钉钉通知")
def periodicalManage_sendDingNotice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodicalManage/sendDingNotice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/管理端/添加内刊")
def periodicalManage_addPeriodical_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodicalManage/addPeriodical"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/管理端/内刊状态分栏")
def periodicalManage_listPeriodicalsOnPubStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodicalManage/listPeriodicalsOnPubStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/管理端/回显内刊")
def periodicalManage_showPeriodicalContent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodicalManage/showPeriodicalContent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/管理端/修改内刊")
def periodicalManage_updatePeriodical_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodicalManage/updatePeriodical"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/管理端/修改内刊状态")
def periodicalManage_updatePeriodicalOnPubStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodicalManage/updatePeriodicalOnPubStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

