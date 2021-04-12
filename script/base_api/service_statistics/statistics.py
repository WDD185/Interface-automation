
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/统计报表/业务统计/2019人次动态")
def statistics_personTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019人次动态"
    url = f"/service-statistics/statistics/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/人次动态历史数据保存")
def statistics_batch_add_personTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/人次动态历史数据保存"
    url = f"/service-statistics/statistics/batch/add/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019人次动态明细导出")
def statistics_export_personTimeDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019人次动态明细导出"
    url = f"/service-statistics/statistics/export/personTimeDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019导出续报率")
def statistics_export_continueRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019导出续报率"
    url = f"/service-statistics/statistics/export/continueRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019查询续报率")
def statistics_query_continue_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019查询续报率"
    url = f"/service-statistics/statistics/query/continue"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表(新)/导出URL查询")
def statistics_export_queryUrl_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表(新)/导出URL查询"
    url = f"/service-statistics/statistics/export/queryUrl"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019人次动态导出")
def statistics_export_personTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019人次动态导出"
    url = f"/service-statistics/statistics/export/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/查询毕业年级")
def statistics_maxGrade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/查询毕业年级"
    url = f"/service-statistics/statistics/maxGrade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019满班率")
def statistics_fullClass_rate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019满班率"
    url = f"/service-statistics/statistics/fullClass/rate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019满班率导出")
def statistics_export_fullClassRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019满班率导出"
    url = f"/service-statistics/statistics/export/fullClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/查询最高班型")
def statistics_maxClassType_queryAll_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/查询最高班型"
    url = f"/service-statistics/statistics/maxClassType/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019退费率导出")
def statistics_export_refundRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019退费率导出"
    url = f"/service-statistics/statistics/export/refundRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/2019退费率")
def statistics_refundRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/2019退费率"
    url = f"/service-statistics/statistics/refundRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/未报名学生返报")
def statistics_return_student_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/未报名学生返报"
    url = f"/service-statistics/statistics/return/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/未报名学生续报")
def statistics_continue_student_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/未报名学生续报"
    url = f"/service-statistics/statistics/continue/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/未报名学生返报导出")
def statistics_export_return_student_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/未报名学生返报导出"
    url = f"/service-statistics/statistics/export/return/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/未报名学生续报导出")
def statistics_export_continue_student_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/未报名学生续报导出"
    url = f"/service-statistics/statistics/export/continue/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/每日班级动态")
def statistics_export_day_data_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/每日班级动态"
    url = f"/service-statistics/statistics/export/day/data"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/导出点名数据")
def statistics_export_day_call_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/导出点名数据"
    url = f"/service-statistics/statistics/export/day/call"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报明细导出")
def statistics_export_continueRateDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/续报明细导出"
    url = f"/service-statistics/statistics/export/continueRateDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/班级报表/退费明细导出")
def statistics_export_refundRateDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/班级报表/退费明细导出"
    url = f"/service-statistics/statistics/export/refundRateDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/预退费明细导出")
def statistics_export_continuePreRefundDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/预退费明细导出"
    url = f"/service-statistics/statistics/export/continuePreRefundDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教师三率")
def statistics_teacherRate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教师三率"
    url = f"/service-statistics/statistics/teacherRate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教师三率/明细")
def statistics_teacherRate_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/教师三率/明细"
    url = f"/service-statistics/statistics/teacherRate/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/绩效统计/提成人次/明细导出")
def statistics_export_commission_personTime_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/绩效统计/提成人次/明细导出"
    url = f"/service-statistics/statistics/export/commission/personTime/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/绩效统计/提成人次/导出")
def statistics_export_commission_personTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/绩效统计/提成人次/导出"
    url = f"/service-statistics/statistics/export/commission/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/绩效统计/提成人次")
def statistics_commission_personTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/绩效统计/提成人次"
    url = f"/service-statistics/statistics/commission/personTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/运营分析/教师效率")
def statistics_running_teacher_efficiency_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/运营分析/教师效率"
    url = f"/service-statistics/statistics/running/teacher/efficiency"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/运营分析/教师效率/导出后")
def statistics_export_running_teacher_efficiency_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/运营分析/教师效率/导出后"
    url = f"/service-statistics/statistics/export/running/teacher/efficiency"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/年级科目续报")
def statistics_export_continueRateGradeSubject_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/年级科目续报"
    url = f"/service-statistics/statistics/export/continueRateGradeSubject"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/导出在读学员数据")
def statistics_export_day_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/导出在读学员数据"
    url = f"/service-statistics/statistics/export/day/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/导出竞品机构")
def statistics_export_exportAgency_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/导出竞品机构"
    url = f"/service-statistics/statistics/export/exportAgency"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/导出公立学校")
def statistics_export_exportSchool_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/导出公立学校"
    url = f"/service-statistics/statistics/export/exportSchool"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/导出周边商机")
def statistics_export_exportAroundBusiness_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/导出周边商机"
    url = f"/service-statistics/statistics/export/exportAroundBusiness"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/其他/导出周边小区")
def statistics_export_exprotAroundEstate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/其他/导出周边小区"
    url = f"/service-statistics/statistics/export/exprotAroundEstate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/运营分析/满班率分析/科目年级满班率")
def statistics_running_fullClass_grade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/运营分析/满班率分析/科目年级满班率"
    url = f"/service-statistics/statistics/running/fullClass/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/运营分析/满班率分析/科目年级满班率/导出")
def statistics_export_running_fullClass_grade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/运营分析/满班率分析/科目年级满班率/导出"
    url = f"/service-statistics/statistics/export/running/fullClass/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/满班率分析/科目学段满班率")
def statistics_running_fullClass_phase_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/满班率分析/科目学段满班率"
    url = f"/service-statistics/statistics/running/fullClass/phase"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/满班率分析/科目学段满班率/导出")
def statistics_export_running_fullClass_phase_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/满班率分析/科目学段满班率/导出"
    url = f"/service-statistics/statistics/export/running/fullClass/phase"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报率分析/科目年级续报率")
def statistics_running_continue_grade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/续报率分析/科目年级续报率"
    url = f"/service-statistics/statistics/running/continue/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报率分析/科目年级续报率/导出")
def statistics_export_running_continue_grade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/续报率分析/科目年级续报率/导出"
    url = f"/service-statistics/statistics/export/running/continue/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报率分析/入口年级转化率")
def statistics_running_continue_entryGrade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/续报率分析/入口年级转化率"
    url = f"/service-statistics/statistics/running/continue/entryGrade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/续报率分析/入口年级转化率/导出")
def statistics_export_running_continue_entryGrade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/续报率分析/入口年级转化率/导出"
    url = f"/service-statistics/statistics/export/running/continue/entryGrade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/退费率分析/科目年级退费率")
def statistics_running_refund_grade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/退费率分析/科目年级退费率"
    url = f"/service-statistics/statistics/running/refund/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/退费率分析/科目年级退费率/导出")
def statistics_export_running_refund_grade_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/退费率分析/科目年级退费率/导出"
    url = f"/service-statistics/statistics/export/running/refund/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/退费率分析/退费率排名")
def statistics_running_refund_rank_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/退费率分析/退费率排名"
    url = f"/service-statistics/statistics/running/refund/rank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/退费率分析/退费率排名/导出")
def statistics_export_running_refund_rank_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/退费率分析/退费率排名/导出"
    url = f"/service-statistics/statistics/export/running/refund/rank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次)")
def statistics_running_studentStructural_times_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次)"
    url = f"/service-statistics/statistics/running/studentStructural/times"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次)/导出")
def statistics_export_running_studentStructural_times_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次)/导出"
    url = f"/service-statistics/statistics/export/running/studentStructural/times"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次占比)")
def statistics_running_studentStructural_rate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次占比)"
    url = f"/service-statistics/statistics/running/studentStructural/rate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次占比)/导出")
def statistics_export_running_studentStructural_rate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/生源结构分析/年级班级结构(人次占比)/导出"
    url = f"/service-statistics/statistics/export/running/studentStructural/rate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/退费报表/财务退费人次")
def statistics_finance_refund_times_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/退费报表/财务退费人次"
    url = f"/service-statistics/statistics/finance/refund/times"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/退费报表/财务退费人次/导出")
def statistics_export_finance_refund_times_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/退费报表/财务退费人次/导出"
    url = f"/service-statistics/statistics/export/finance/refund/times"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/预收动态")
def statistics_finance_advanceIncome_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/预收动态"
    url = f"/service-statistics/statistics/finance/advanceIncome"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/预收动态导出")
def statistics_export_finance_advanceIncome_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/预收动态导出"
    url = f"/service-statistics/statistics/export/finance/advanceIncome"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/营收动态")
def statistics_finance_revenue_trends_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/营收动态"
    url = f"/service-statistics/statistics/finance/revenue/trends"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/营收动态")
def statistics_export_finance_revenue_trends_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/营收动态"
    url = f"/service-statistics/statistics/export/finance/revenue/trends"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/退费报表/退费金额汇总")
def statistics_finance_refund_summary_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/退费报表/退费金额汇总"
    url = f"/service-statistics/statistics/finance/refund/summary"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/财务报表/退费报表/退费金额汇总/导出")
def statistics_export_finance_refund_summary_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/财务报表/退费报表/退费金额汇总/导出"
    url = f"/service-statistics/statistics/export/finance/refund/summary"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/补费率查询")
def statistics_supplementaryPayment_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/补费率查询"
    url = f"/service-statistics/statistics/supplementaryPayment"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/补费率导出")
def statistics_export_supplementaryPayment_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/补费率导出"
    url = f"/service-statistics/statistics/export/supplementaryPayment"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/补费率明细导出")
def statistics_export_supplementaryPayment_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/补费率明细导出"
    url = f"/service-statistics/statistics/export/supplementaryPayment/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/绩效统计/个人提成人次")
def statistics_commission_personTime_personal_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/绩效统计/个人提成人次"
    url = f"/service-statistics/statistics/commission/personTime/personal"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/绩效统计/个人提成人次/导出")
def statistics_export_commission_personTime_personal_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/绩效统计/个人提成人次/导出"
    url = f"/service-statistics/statistics/export/commission/personTime/personal"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/绩效统计/个人提成人次/导出明细")
def statistics_export_commission_personTime_personal_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/绩效统计/个人提成人次/导出明细"
    url = f"/service-statistics/statistics/export/commission/personTime/personal/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/收据明细导出")
def statistics_export_advance_charge_receipt_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/收费报表/收据明细导出"
    url = f"/service-statistics/statistics/export/advance/charge/receipt"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/收费报表/收据明细")
def statistics_advance_charge_receipt_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/收费报表/收据明细"
    url = f"/service-statistics/statistics/advance/charge/receipt"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/运营分析/班课到课率")
def statistics_running_student_arriveClassRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/运营分析/班课到课率"
    url = f"/service-statistics/statistics/running/student/arriveClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/运营分析/班课到课率/导出")
def statistics_export_running_student_arriveClassRate_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/运营分析/班课到课率/导出"
    url = f"/service-statistics/statistics/export/running/student/arriveClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/统计报表/业务统计/满班率明细导出")
def statistics_export_fullClassRate_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/业务统计/满班率明细导出"
    url = f"/service-statistics/statistics/export/fullClassRate/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

