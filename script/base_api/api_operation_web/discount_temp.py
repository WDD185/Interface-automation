
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/优惠设置/优惠/查询单个优惠")
def discount_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/查询优惠列表")
def discount_queryAll_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/查看单个优惠操作记录")
def discount_queryOperationRecordByDiscountId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/queryOperationRecordByDiscountId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/编辑优惠")
def discount_edit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/更改优惠状态")
def discount_updateStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/修改备注")
def discount_updateRemark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/updateRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/新增优惠")
def discount_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/discount/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/新增优惠")
def discount_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/查询优惠列表")
def discount_queryAll_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/查看单个优惠操作记录")
def discount_queryOperationRecordByDiscountId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/queryOperationRecordByDiscountId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/编辑优惠")
def discount_edit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/更改优惠状态")
def discount_updateStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/修改备注")
def discount_updateRemark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/updateRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/查询单个优惠")
def discount_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/discount/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

