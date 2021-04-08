
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/金钱/支付")
def payments_response_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/payments/response"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

