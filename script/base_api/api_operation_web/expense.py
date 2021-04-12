
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/财务报表/课消报表/学员费用预警-查询")
def expense_warning_queryStudentExpenseWarning_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务报表/课消报表/学员费用预警-查询"
    url = f"/api-operation-web/expense/warning/queryStudentExpenseWarning"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务报表/课消报表/校区费用预警-查询")
def expense_warning_querySchoolExpenseWarning_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务报表/课消报表/校区费用预警-查询"
    url = f"/api-operation-web/expense/warning/querySchoolExpenseWarning"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

