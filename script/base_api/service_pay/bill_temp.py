
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("退款异常对账查询")
def bill_get_refund_mistakes_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/bill/get-refund-mistakes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("异常处理接口")
def bill_deal_refund_mistakes_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/bill/deal-refund-mistakes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("退款异常导出接口")
def bill_bill_error_export_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/bill/bill-error-export"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

