
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("制度管理/根据状态查询列表")
def regimeManage_listRegimesOnPubStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/regimeManage/listRegimesOnPubStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/更新状态")
def regimeManage_updateRegimeOnPubStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/regimeManage/updateRegimeOnPubStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/新增制度")
def regimeManage_addRegime_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/regimeManage/addRegime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/制度查询")
def regimeManage_showRegimeContent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/regimeManage/showRegimeContent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/更新制度")
def regimeManage_updateRegime_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/regimeManage/updateRegime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/发送通知")
def regimeManage_sendDingNotice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/regimeManage/sendDingNotice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

