
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/订单/根据订单状态查询订单数量")
def order_api_inner_order_order_countByStatuses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order-api/inner-order/order/countByStatuses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠券/优惠券查询服务")
def order_api_inner_order_queryCoupon_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order-api/inner-order/queryCoupon"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

