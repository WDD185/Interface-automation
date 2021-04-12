
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/统计报表/班级报表/固化班级花名册-查询")
def report_queryClassRegister_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/固化班级花名册-查询"
    url = f"/api-operation-web/report/queryClassRegister"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

