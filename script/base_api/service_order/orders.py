
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/订单管理/订单作废")
def orders_cancle_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/订单作废"
    url = f"/service-order/orders/cancle"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

