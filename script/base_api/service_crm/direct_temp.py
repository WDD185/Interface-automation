
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/报表/运营分析列表查询")
def direct_report_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/direct/report/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/运营分析列表导出")
def direct_report_export_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/direct/report/export"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/课程顾问明细导出")
def direct_report_exportDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/direct/report/exportDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/运营分析/教师沟通分析列表查询")
def direct_report_queryByTeacher_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/direct/report/queryByTeacher"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/运营分析/导出教师沟通分析")
def direct_report_exportByTeacher_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/direct/report/exportByTeacher"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/运营分析/导出教师沟通分析详情")
def direct_report_exportDetailByTeacher_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_crm/direct/report/exportDetailByTeacher"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

