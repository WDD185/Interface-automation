
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/购课单/购课单列表")
def applet_getPurchaseOrderList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/applet/getPurchaseOrderList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/购课单数量")
def applet_purchaseOrder_studentId_student_count_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/applet/purchaseOrder/{studentId}/student/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/添加购课单")
def applet_purchaseOrder_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/applet/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/删除购课单")
def applet_purchaseOrder_studentId_student_delete(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/applet/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/购课单/班级座次")
def applet_classes_classId_seats_get(classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/applet/classes/{classId}/seats"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/电子钱包余额")
def applet_financial_wallet_remain_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/applet/financial/wallet/remain"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

