
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/营销中心/分销业务统计/统计列表")
def shareEvent_shareCountList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/分销业务统计/统计列表"
    url = f"/service-gos/shareEvent/shareCountList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/分销业务统计/统计列表导出")
def shareEvent_shareCountListExport_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/分销业务统计/统计列表导出"
    url = f"/service-gos/shareEvent/shareCountListExport"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

