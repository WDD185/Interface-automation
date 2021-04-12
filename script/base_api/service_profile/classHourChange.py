
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/财务管理/课消变动记录/取消点名")
def classHourChange_rollCallCancel_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/课消变动记录/取消点名"
    url = f"/service-profile/classHourChange/rollCallCancel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/课消变动记录/点名")
def classHourChange_rollCall_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/课消变动记录/点名"
    url = f"/service-profile/classHourChange/rollCall"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/课消变动记录/课消变动")
def classHourChange_change_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/课消变动记录/课消变动"
    url = f"/service-profile/classHourChange/change"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

