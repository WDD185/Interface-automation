
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("微信JS支付退款回调")
def refund_callback_wechat_jsapi_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "微信JS支付退款回调"
    url = f"/service-pay/refund/callback/wechat/jsapi"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

