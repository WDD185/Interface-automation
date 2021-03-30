
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/入学诊断/诊断列表查询")
def diagnosis_queryDiagnosticDetailList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/diagnosis/queryDiagnosticDetailList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/入学诊断/查询诊断名单学生信息")
def diagnosis_queryDiagnosticStudentsPageList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/diagnosis/queryDiagnosticStudentsPageList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/入学诊断/获取试卷")
def diagnosis_exam_paper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/diagnosis/exam/paper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/入学诊断/查询诊断报告详情")
def diagnosis_report_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/diagnosis/report/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

