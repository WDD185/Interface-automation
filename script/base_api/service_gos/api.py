
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("线上商店-通用接口/获取省市区")
def api_general_listAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/api/general/listAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-通用接口/获取校区")
def api_general_listSchoolAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/api/general/listSchoolAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

