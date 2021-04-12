
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/结转/新增结转")
def finance_return_carryover_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/结转/新增结转"
    url = f"/service-profile/finance/return/carryover"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/查询可退费")
def finance_refund_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/退费/查询可退费"
    url = f"/service-profile/finance/refund/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/新增退费")
def finance_return_refund_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/退费/新增退费"
    url = f"/service-profile/finance/return/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转/查询可结转")
def finance_carryover_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/结转/查询可结转"
    url = f"/service-profile/finance/carryover/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退费操作")
def finance_apply_refund_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/退费操作"
    url = f"/service-profile/finance/apply/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退费审批操作")
def finance_approve_refund_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/退费审批操作"
    url = f"/service-profile/finance/approve/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/重新提交退费操作")
def finance_resubmit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/重新提交退费操作"
    url = f"/service-profile/finance/resubmit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转申请操作")
def finance_apply_carryover_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/结转申请操作"
    url = f"/service-profile/finance/apply/carryover"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("金蝶退费回调接口")
def finance_callbackPayStatusToKingdee_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "金蝶退费回调接口"
    url = f"/service-profile/finance/callbackPayStatusToKingdee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

