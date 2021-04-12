
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/财务报表/预收报表/收据明细-查询")
def charge_receipt_queryReceiptReports_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务报表/预收报表/收据明细-查询"
    url = f"/api-operation-web/charge/receipt/queryReceiptReports"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

