
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/营销中心/banner管理/banner列表")
def banner_pageList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/banner/pageList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/banner管理/banner图列表")
def banner_item_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/banner/item/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/banner管理/新增banner图")
def banner_item_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/banner/item/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/banner管理/修改banner图")
def banner_item_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/banner/item/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/banner管理/启停banner图")
def banner_item_switch_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/banner/item/switch"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/banner管理/删除banner图")
def banner_item_delete_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/banner/item/delete"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

