
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/设置/优惠设置/转介绍领取设置/操作日志查询")
def introduce_rule_operation_list_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/设置/优惠设置/转介绍领取设置/操作日志查询"
    url = f"/api-operation-web/introduce/rule/operation/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

