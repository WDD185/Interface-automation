
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/关于极客/栏目列表")
def company_column_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/关于极客/栏目列表"
    url = f"/service-user/company/column/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/关于极客/修改栏目")
def company_column_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/关于极客/修改栏目"
    url = f"/service-user/company/column/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/关于极客/启停栏目")
def company_column_switch_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/关于极客/启停栏目"
    url = f"/service-user/company/column/switch"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

