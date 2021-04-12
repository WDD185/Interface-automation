
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("线上商店-通用接口/获取省市区")
def api_general_listAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-通用接口/获取省市区"
    url = f"/service-gos/api/general/listAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-通用接口/获取校区")
def api_general_listSchoolAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-通用接口/获取校区"
    url = f"/service-gos/api/general/listSchoolAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

