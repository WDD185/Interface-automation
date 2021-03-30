
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("中行pos支付回调")
def callback_boc_pos_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/boc/pos"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信支付回调")
def callback_wechat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/wechat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝支付回调")
def callback_alipay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/alipay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信JS支付回调")
def callback_wechat_jsapi_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/wechat/jsapi"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信扫码支付-回调接口")
def callback_wechat_scan_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/wechat/scan"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝扫码支付-回调接口")
def callback_alipay_scan_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/alipay/scan"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝h5支付-回调接口")
def callback_alipay_h5_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/callback/alipay/h5"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

