
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/财务管理/库存现金/查询库存现金记录")
def handCash_queryRecord_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/库存现金/查询库存现金记录"
    url = f"/service-finance/handCash/queryRecord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

