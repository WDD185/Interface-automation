
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/退电子钱包操作")
def v2_finance_refund_studentAccount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/退电子钱包操作"
    url = f"/service-finance/v2/finance/refund/studentAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

