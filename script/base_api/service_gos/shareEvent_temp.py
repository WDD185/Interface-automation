
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/营销中心/分销业务统计/统计列表")
def shareEvent_shareCountList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/shareEvent/shareCountList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/分销业务统计/统计列表导出")
def shareEvent_shareCountListExport_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/shareEvent/shareCountListExport"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

