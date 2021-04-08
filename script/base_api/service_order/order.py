
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/报名/pc端获取可使用优惠及优惠券")
def order_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/报名/订单/新增订单")
def order_saveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/修改备注")
def order_modifyRemark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/modifyRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/pc端下单前的预验证")
def order_preValidOrderCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/报名/订单/计算订单总价(旧)")
def order_countOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/countOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/报名/订单/计算订单总价")
def order_calculateOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/订单状态修改")
def order_app_updateStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/app/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/查询订单")
def order_app_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/app/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/验证学生重复生成订单")
def order_app_studentHasOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/app/studentHasOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/修改收据")
def order_modifyFinancialFlow_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/modifyFinancialFlow"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/查询订单详情")
def order_queryOrderDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/queryOrderDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/老pos订单支付")
def order_orderPay_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/orderPay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/报名/订单/查询单个订单")
def order_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/查询订单状态")
def order_app_queryStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/app/queryStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/获取可使用优惠")
def order_discounts_queryMatchDiscount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/discounts/queryMatchDiscount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单/查询订单")
def order_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/订单状态修改")
def order_updateStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/验证学生重复生成订单")
def order_studentHasOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/studentHasOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/二维码查询订单")
def order_qr_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/qr/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/计算订单总价(旧)")
def order_app_countOrderPrice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/app/countOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/报名/订单/新增订单(旧)")
def order_save_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/新增订单(旧)")
def order_app_save_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/app/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("订单/查询订单状态")
def order_queryStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/queryStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("订单/支付/预支付")
def order_pay_prePay_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/pay/prePay"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/支付/重新支付")
def order_pay_rePrePay_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/pay/rePrePay"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/APP重新支付")
def order_pay_appReprePay_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/pay/appReprePay"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/校区/订单管理/重新支付校验")
def order_pay_reCheck_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/order/pay/reCheck"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

