
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/报表/课消报表/学生费用预警")
def report_finance_student_expense_warning_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/finance/student/expense/warning"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/收费报表/查询学生电子钱包汇总")
def report_finance_student_summary_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/finance/student/summary"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/班级人数")
def report_class_classNum_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/class/classNum"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/出勤明细")
def report_class_classAttendance_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/class/classAttendance"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/课消报表/校区费用预警")
def report_finance_school_expense_warning_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/finance/school/expense/warning"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/收费报表/查询学生电子钱包明细")
def report_finance_student_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/finance/student/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/学员课消明细日志")
def report_consumption_student_detail_log_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/consumption/student/detail/log"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/获取全部方案")
def report_dynamic_allTarget_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/allTarget"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/获取默认方案")
def report_dynamic_defTarget_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/defTarget"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/课消总汇")
def report_consumption_all_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/consumption/all"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/学员课消明细")
def report_consumption_student_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/consumption/student/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/材料收费")
def report_charge_material_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/charge/material"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/学员课消总汇")
def report_consumption_student_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/consumption/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/违规统计/违规班贴")
def report_violation_classPost_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/violation/classPost"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/班级花名册")
def report_class_classRegister_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/class/classRegister"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/课程收费")
def report_charge_course_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/charge/course"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报率")
def report_dynamic_continueRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/continueRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/筛选条件/更多筛选")
def report_condition_more_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/condition/more"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/退费率")
def report_dynamic_refundRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/refundRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/满班率")
def report_dynamic_fullClassRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/fullClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/续班率日报")
def report_class_daylyReportExcelExport_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/class/daylyReportExcelExport"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/营收动态")
def report_dynamic_revenue_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/revenue"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/退费汇总")
def report_charge_refund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/charge/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/筛选条件/选择班级")
def report_condition_class_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/condition/class"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/违规统计/违规点名")
def report_violation_rollCall_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/violation/rollCall"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/筛选条件/选择课程")
def report_condition_course_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/condition/course"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/人次动态")
def report_dynamic_personTime_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/dynamic/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("收入报表-学员收入列表")
def report_finance_student_income_list_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/finance/student/income/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("收入报表-校区收入列表")
def report_finance_school_income_list_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/report/finance/school/income/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/固化班级花名册-查询")
def report_queryClassRegister_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/report/queryClassRegister"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

