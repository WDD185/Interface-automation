
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/我的/电子钱包余额")
def app_financial_epayDeductionByStudentIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-finance/app/financial/epayDeductionByStudentIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/用户转介绍金额")
def app_finance_introduce_user_amount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-finance/app/finance/introduce/user/amount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/领取至电子钱包")
def app_finance_introduce_receive_receiveToWallet_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-finance/app/finance/introduce/receive/receiveToWallet"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/电子钱包/流水")
def app_financial_wallet_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-finance/app/financial/wallet/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/明细列表")
def app_finance_introduce_receive_introduced_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-finance/app/finance/introduce/receive/introduced/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/发放明细")
def app_finance_introduce_receive_query_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-finance/app/finance/introduce/receive/query/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

