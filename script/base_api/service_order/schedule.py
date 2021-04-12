
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/订单/释放座位")
def schedule_cancle_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单/释放座位"
    url = f"/service-order/schedule/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单/预占座位")
def schedule_take_seat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单/预占座位"
    url = f"/service-order/schedule/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

