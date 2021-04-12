
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("备课/下载打点")
def dowLogController_printLog_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "备课/下载打点"
    url = f"/service-research/dowLogController/printLog"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

