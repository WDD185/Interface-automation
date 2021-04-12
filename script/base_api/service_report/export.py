
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/财务管理/对账/导出对账记录")
def export_finance_accountingRecord_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/对账/导出对账记录"
    url = f"/service-report/export/finance/accountingRecord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/人次动态明细导出")
def export_report_personTime_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/人次动态明细导出"
    url = f"/service-report/export/report/personTime/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/班级人数-导出报表")
def export_report_class_classNum_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/班级人数-导出报表"
    url = f"/service-report/export/report/class/classNum"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/班级花名册-导出报表")
def export_report_class_classRegister_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/班级花名册-导出报表"
    url = f"/service-report/export/report/class/classRegister"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/出勤明细-导出报表")
def export_report_class_classAttendance_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/出勤明细-导出报表"
    url = f"/service-report/export/report/class/classAttendance"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/收据导出")
def export_report_charge_completedOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/收费报表/收据导出"
    url = f"/service-report/export/report/charge/completedOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("导出/题目word导出")
def export_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "导出/题目word导出"
    url = f"/service-report/export/question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/课消报表/学生费用预警导出")
def export_student_expense_warning_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/报表/课消报表/学生费用预警导出"
    url = f"/service-report/export/student/expense/warning"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/导出/课件库/文件查阅导出")
def export_lessons_textbook_exportReadCheck_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/导出/课件库/文件查阅导出"
    url = f"/service-report/export/lessons/textbook/exportReadCheck"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/导出/课件库/文件未查阅导出")
def export_lessons_textbook_exportReadCheckUnRead_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/导出/课件库/文件未查阅导出"
    url = f"/service-report/export/lessons/textbook/exportReadCheckUnRead"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/课消报表/校区费用预警导出")
def export_school_expense_warning_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/报表/课消报表/校区费用预警导出"
    url = f"/service-report/export/school/expense/warning"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/学员课消明细日志导出")
def export_report_consumption_student_detail_log_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/课消报表/学员课消明细日志导出"
    url = f"/service-report/export/report/consumption/student/detail/log"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/收费报表/学生电子钱包汇总导出")
def export_student_account_summary_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/报表/收费报表/学生电子钱包汇总导出"
    url = f"/service-report/export/student/account/summary"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/导出学生优惠券")
def export_order_coupon_exportUsedCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/优惠设置/优惠券/导出学生优惠券"
    url = f"/service-report/export/order/coupon/exportUsedCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/排课/导出排课")
def export_education_schedule_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教务管理/排课/导出排课"
    url = f"/service-report/export/education/schedule"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/退费汇总导出")
def export_report_charge_refund_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/收费报表/退费汇总导出"
    url = f"/service-report/export/report/charge/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/材料收费导出")
def export_report_charge_material_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/收费报表/材料收费导出"
    url = f"/service-report/export/report/charge/material"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/导出退余额记录")
def export_finance_eWallet_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/退费/导出退余额记录"
    url = f"/service-report/export/finance/eWallet"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/违规统计/违规点名导出")
def export_report_violation_rollCall_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/违规统计/违规点名导出"
    url = f"/service-report/export/report/violation/rollCall"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/人次动态导出")
def export_report_personTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/人次动态导出"
    url = f"/service-report/export/report/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/营收动态报表导出")
def export_report_revenue_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/营收动态报表导出"
    url = f"/service-report/export/report/revenue"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/学员课消总汇导出")
def export_report_consumption_student_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/课消报表/学员课消总汇导出"
    url = f"/service-report/export/report/consumption/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/班级/导出班级")
def export_education_class_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教务管理/班级/导出班级"
    url = f"/service-report/export/education/class"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/库存现金/导出库存现金")
def export_finance_handCash_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/库存现金/导出库存现金"
    url = f"/service-report/export/finance/handCash"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报率导出")
def export_report_continueRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/续报率导出"
    url = f"/service-report/export/report/continueRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/退费率导出")
def export_report_refundRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/退费率导出"
    url = f"/service-report/export/report/refundRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/违规统计/违规班贴导出")
def export_report_violation_classPost_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/违规统计/违规班贴导出"
    url = f"/service-report/export/report/violation/classPost"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/课程收费导出")
def export_report_charge_course_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/收费报表/课程收费导出"
    url = f"/service-report/export/report/charge/course"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/缴款确认/导出缴款")
def export_finance_payin_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/缴款确认/导出缴款"
    url = f"/service-report/export/finance/payin"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/订单管理/导出订单")
def export_order_queryOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/订单管理/导出订单"
    url = f"/service-report/export/order/queryOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/课程/导出课程")
def export_education_course_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教务管理/课程/导出课程"
    url = f"/service-report/export/education/course"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/学员课消明细导出")
def export_report_consumption_student_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/课消报表/学员课消明细导出"
    url = f"/service-report/export/report/consumption/student/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/导出/查询导出地址")
def export_queryUrl_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/导出/查询导出地址"
    url = f"/service-report/export/queryUrl"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/课消报表/课消总汇导出")
def export_report_consumption_all_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/课消报表/课消总汇导出"
    url = f"/service-report/export/report/consumption/all"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/满班率导出")
def export_report_fullClassRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/满班率导出"
    url = f"/service-report/export/report/fullClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/收支流水/导出收支流水")
def export_finance_financialFlow_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/收支流水/导出收支流水"
    url = f"/service-report/export/finance/financialFlow"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/导出退费记录")
def export_finance_refund_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/财务管理/退费/导出退费记录"
    url = f"/service-report/export/finance/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/报表/收费报表/学生电子钱包明细导出")
def export_student_account_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/报表/收费报表/学生电子钱包明细导出"
    url = f"/service-report/export/student/account/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审阅/教案导出")
def export_teaching_plans_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/备课审阅/教案导出"
    url = f"/service-report/export/teaching_plans"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审阅/刷题导出")
def export_teaching_exercises_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/备课审阅/刷题导出"
    url = f"/service-report/export/teaching_exercises"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课统计/教案导出")
def export_teaching_plans_statistics_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/备课统计/教案导出"
    url = f"/service-report/export/teaching_plans/statistics"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课统计/刷题导出")
def export_teaching_exercises_statistics_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/备课统计/刷题导出"
    url = f"/service-report/export/teaching_exercises/statistics"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/上课/埋点导出")
def export_statistical_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/上课/埋点导出"
    url = f"/service-report/export/statistical"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转/导出结转记录")
def export_finance_carryOver_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/结转/导出结转记录"
    url = f"/service-report/export/finance/carryOver"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账/异常对账单/导出")
def export_pay_checkBill_exportMistake_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "分账/异常对账单/导出"
    url = f"/service-report/export/pay/checkBill/exportMistake"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/公立学校/导出列表")
def export_systemSettings_schools_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/公立学校/导出列表"
    url = f"/service-report/export/systemSettings/schools"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/学生信息/导出学生信息")
def export_student_items_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/学生信息/导出学生信息"
    url = f"/service-report/export/student/items"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("异常导出接口")
def export_pay_checkBill_export_refund_mistake_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "异常导出接口"
    url = f"/service-report/export/pay/checkBill/export-refund-mistake"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("收入报表-学员收入列表导出")
def export_report_student_income_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "收入报表-学员收入列表导出"
    url = f"/service-report/export/report/student/income"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("收入报表-校区收入列表导出")
def export_report_school_income_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "收入报表-校区收入列表导出"
    url = f"/service-report/export/report/school/income"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额-处理列表-导出")
def export_report_introduce_record_deal_receive_list_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "转介绍金额-处理列表-导出"
    url = f"/service-report/export/report/introduce/record/deal/receive/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/消息列表/自定义消息/下载明细")
def export_message_messageId_sendCustomMessageDetail_post(messageId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "设置/消息/消息列表/自定义消息/下载明细"
    url = f"/service-report/export/message/{messageId}/sendCustomMessageDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("设置/消息/消息列表/自定义消息/下载明细")
def export_message_messageId_sendSystemMessageDetail_post(messageId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "设置/消息/消息列表/自定义消息/下载明细"
    url = f"/service-report/export/message/{messageId}/sendSystemMessageDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任CRM/学员管理/我的班级/导出班主任有的班级")
def export_education_class_directorId_post(directorId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任CRM/学员管理/我的班级/导出班主任有的班级"
    url = f"/service-report/export/education/class/{directorId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任CRM/学员管理/我的班级/学员列表导出")
def export_education_student_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任CRM/学员管理/我的班级/学员列表导出"
    url = f"/service-report/export/education/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额-学员发放汇总-导出")
def export_report_introduce_record_deal_receive_list_collection_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "转介绍金额-学员发放汇总-导出"
    url = f"/service-report/export/report/introduce/record/deal/receive/list-collection"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/入学诊断/诊断名单导出")
def export_diagnosis_students_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/入学诊断/诊断名单导出"
    url = f"/service-report/export/diagnosis/students"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/业绩归属/业绩归属导出")
def export_performance_detailInfo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/业绩归属/业绩归属导出"
    url = f"/service-report/export/performance/detailInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/发送明细下载")
def export_banner_popup_sendList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/发送明细下载"
    url = f"/service-report/export/banner/popup/sendList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/班级花名册-导出电话")
def export_report_class_classRegisterContainPhoneNo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/班级花名册-导出电话"
    url = f"/service-report/export/report/class/classRegisterContainPhoneNo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

