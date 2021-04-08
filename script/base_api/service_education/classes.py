
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/优惠设置/新增优惠(旧)")
def classes_discounts_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/classes/discounts/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/删除优惠(旧)")
def classes_discounts_delete_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/classes/discounts/delete"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/查询优惠(旧)")
def classes_discounts_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/classes/discounts/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/修改优惠(旧)")
def classes_discounts_update_put(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):    
    url = host + f"/service-education/classes/discounts/update"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/订单班级验证")
def classes_discounts_discount_valideClass_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/classes/discounts/discount/valideClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/优惠匹配")
def classes_discounts_discount_calculate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/classes/discounts/discount/calculate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/查询材料费")
def classes_discounts_material_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/classes/discounts/material"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

