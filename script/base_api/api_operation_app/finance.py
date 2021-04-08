
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营APP查询学生电子钱包")
def finance_query_student_school_account_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/finance/query/student/school/account"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP查询学生电子钱包详情")
def finance_query_student_account_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/finance/query/student/account/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP查询学生电子钱包汇总")
def finance_query_student_account_sum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/finance/query/student/account/sum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

