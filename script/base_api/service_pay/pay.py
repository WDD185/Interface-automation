
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("中行POS支付-查询可用pos")
def pay_boc_pos_posInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "中行POS支付-查询可用pos"
    url = f"/service-pay/pay/boc/pos/posInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/主动查询指定支付状态")
def pay_queryPayStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/主动查询指定支付状态"
    url = f"/service-pay/pay/queryPayStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信支付-预支付")
def pay_weChat_app_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "微信支付-预支付"
    url = f"/service-pay/pay/weChat/app/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信支付-对账单")
def pay_weChat_app_conciliation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "微信支付-对账单"
    url = f"/service-pay/pay/weChat/app/conciliation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("中行POS支付-预支付")
def pay_boc_pos_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "中行POS支付-预支付"
    url = f"/service-pay/pay/boc/pos/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信直连支付-预支付")
def pay_weChat_jsapi_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "微信直连支付-预支付"
    url = f"/service-pay/pay/weChat/jsapi/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝支付-预支付")
def pay_ali_app_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "支付宝支付-预支付"
    url = f"/service-pay/pay/ali/app/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("对账/异常账单/更新状态")
def pay_check_mistake_updateMistakeBill_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "对账/异常账单/更新状态"
    url = f"/service-pay/pay/check/mistake/updateMistakeBill"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("对账/异常对账单/列表页")
def pay_check_mistake_queryByBankType_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "对账/异常对账单/列表页"
    url = f"/service-pay/pay/check/mistake/queryByBankType"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/根据公司ID查询校区")
def pay_schoolMerchant_getSchoolAreaByCompId_compId_get(compId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "分账逻辑/配置商户号/根据公司ID查询校区"
    url = f"/service-pay/pay/schoolMerchant/getSchoolAreaByCompId/{compId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/查询所有公司")
def pay_schoolMerchant_queryAllCompany_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "分账逻辑/配置商户号/查询所有公司"
    url = f"/service-pay/pay/schoolMerchant/queryAllCompany"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/修改账户信息")
def pay_schoolMerchant_updateSchoolMerchant_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "分账逻辑/配置商户号/修改账户信息"
    url = f"/service-pay/pay/schoolMerchant/updateSchoolMerchant"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/查询可用账号")
def pay_schoolMerchant_queryByMerchantTypeAndSchoolArea_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "分账逻辑/配置商户号/查询可用账号"
    url = f"/service-pay/pay/schoolMerchant/queryByMerchantTypeAndSchoolArea"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝H5支付-预支付")
def pay_ali_js_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "支付宝H5支付-预支付"
    url = f"/service-pay/pay/ali/js/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝扫码支付-预支付")
def pay_ali_scan_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "支付宝扫码支付-预支付"
    url = f"/service-pay/pay/ali/scan/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信扫码支付-预支付")
def pay_wechat_scan_prepay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "微信扫码支付-预支付"
    url = f"/service-pay/pay/wechat/scan/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

