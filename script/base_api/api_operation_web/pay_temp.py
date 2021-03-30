
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("中行POS支付-查询可用pos")
def pay_boc_pos_posInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/boc/pos/posInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/主动查询指定支付状态")
def pay_queryPayStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/queryPayStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信支付-预支付")
def pay_weChat_app_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/weChat/app/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信支付-对账单")
def pay_weChat_app_conciliation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/weChat/app/conciliation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("中行POS支付-预支付")
def pay_boc_pos_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/boc/pos/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信直连支付-预支付")
def pay_weChat_jsapi_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/weChat/jsapi/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝支付-预支付")
def pay_ali_app_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/ali/app/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("对账/异常账单/更新状态")
def pay_check_mistake_updateMistakeBill_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/check/mistake/updateMistakeBill"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("对账/异常对账单/列表页")
def pay_check_mistake_queryByBankType_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/check/mistake/queryByBankType"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/根据公司ID查询校区")
def pay_schoolMerchant_getSchoolAreaByCompId_compId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/schoolMerchant/getSchoolAreaByCompId/{compId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/查询所有公司")
def pay_schoolMerchant_queryAllCompany_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/schoolMerchant/queryAllCompany"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/修改账户信息")
def pay_schoolMerchant_updateSchoolMerchant_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/schoolMerchant/updateSchoolMerchant"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/配置商户号/查询可用账号")
def pay_schoolMerchant_queryByMerchantTypeAndSchoolArea_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/schoolMerchant/queryByMerchantTypeAndSchoolArea"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝H5支付-预支付")
def pay_ali_js_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/ali/js/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("支付宝扫码支付-预支付")
def pay_ali_scan_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/ali/scan/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("微信扫码支付-预支付")
def pay_wechat_scan_prepay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_pay/pay/wechat/scan/prepay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/发起支付")
def pay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/pay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/订单管理/订单/发起支付")
def pay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/pay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/h5页面支付")
def pay_H5_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/pay/H5"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/发起支付")
def pay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/pay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/发起支付")
def pay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/pay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/试验产品支付回调")
def pay_callback_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_idea/pay/callback"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

