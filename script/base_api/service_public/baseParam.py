
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/通用/查询行政区域")
def baseParam_queryAdministrativeArea_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/通用/查询行政区域"
    url = f"/service-public/baseParam/queryAdministrativeArea"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

