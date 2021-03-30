
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/营销中心/业绩归属/修改介绍人")
def web_performance_change_employee_id_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/web/performance/change/employee/id"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/业绩归属/修改业绩归属人")
def web_performance_change_introducerStudent_id_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/web/performance/change/introducerStudent/id"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/业绩归属/业绩归属明细")
def web_performance_queryOrderDetailList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/web/performance/queryOrderDetailList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/业绩归属/无业绩归属人明细")
def web_performance_queryPerformanceDetailList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/web/performance/queryPerformanceDetailList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

