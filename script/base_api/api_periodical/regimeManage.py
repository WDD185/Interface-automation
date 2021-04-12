
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("制度管理/根据状态查询列表")
def regimeManage_listRegimesOnPubStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "制度管理/根据状态查询列表"
    url = f"/api-periodical/regimeManage/listRegimesOnPubStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/更新状态")
def regimeManage_updateRegimeOnPubStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "制度管理/更新状态"
    url = f"/api-periodical/regimeManage/updateRegimeOnPubStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/新增制度")
def regimeManage_addRegime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "制度管理/新增制度"
    url = f"/api-periodical/regimeManage/addRegime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/制度查询")
def regimeManage_showRegimeContent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "制度管理/制度查询"
    url = f"/api-periodical/regimeManage/showRegimeContent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/更新制度")
def regimeManage_updateRegime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "制度管理/更新制度"
    url = f"/api-periodical/regimeManage/updateRegime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("制度管理/发送通知")
def regimeManage_sendDingNotice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "制度管理/发送通知"
    url = f"/api-periodical/regimeManage/sendDingNotice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

