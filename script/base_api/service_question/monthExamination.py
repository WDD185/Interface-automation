
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极教研/月考/创建考试")
def monthExamination_pc_addMonthOnlineExam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/创建考试"
    url = f"/service-question/monthExamination/pc/addMonthOnlineExam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/试卷列表")
def monthExamination_pc_getMonthOnlineExamPaperList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/试卷列表"
    url = f"/service-question/monthExamination/pc/getMonthOnlineExamPaperList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/月考列表")
def monthExamination_pc_getMonthOnlineExamList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/月考列表"
    url = f"/service-question/monthExamination/pc/getMonthOnlineExamList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/编辑考试")
def monthExamination_pc_modMonthOnlineExam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/编辑考试"
    url = f"/service-question/monthExamination/pc/modMonthOnlineExam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/考试操作日志")
def monthExamination_pc_getMonthOnlineExamOperationLogList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/考试操作日志"
    url = f"/service-question/monthExamination/pc/getMonthOnlineExamOperationLogList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/删除考试")
def monthExamination_pc_delMonthOnlineExam_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/删除考试"
    url = f"/service-question/monthExamination/pc/delMonthOnlineExam"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/验证考试属性与试卷属性是否一致")
def monthExamination_pc_checkMonthOnlineExamAndPaper_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/验证考试属性与试卷属性是否一致"
    url = f"/service-question/monthExamination/pc/checkMonthOnlineExamAndPaper"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/成绩列表")
def monthExamination_pc_getMonthOnlineExamGradeList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/成绩列表"
    url = f"/service-question/monthExamination/pc/getMonthOnlineExamGradeList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/成绩列表导出")
def monthExamination_pc_getMonthOnlineExamGradeListExport_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/成绩列表导出"
    url = f"/service-question/monthExamination/pc/getMonthOnlineExamGradeListExport"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/月考/考试成绩统计")
def monthExamination_pc_getMonthOnlineExamGradeTotal_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研/月考/考试成绩统计"
    url = f"/service-question/monthExamination/pc/getMonthOnlineExamGradeTotal"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/获取学生的月考列表")
def monthExamination_app_getMonthOnlineExamAppList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/获取学生的月考列表"
    url = f"/service-question/monthExamination/app/getMonthOnlineExamAppList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/根据考试id获取试卷详情")
def monthExamination_app_getMonthOnlineExamPaperInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/根据考试id获取试卷详情"
    url = f"/service-question/monthExamination/app/getMonthOnlineExamPaperInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/根据考试id获取考试信息")
def monthExamination_app_getMonthOnlineExamInfoApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/根据考试id获取考试信息"
    url = f"/service-question/monthExamination/app/getMonthOnlineExamInfoApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/参加考试")
def monthExamination_app_attendMonthExam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/参加考试"
    url = f"/service-question/monthExamination/app/attendMonthExam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/提交答案")
def monthExamination_app_commitMonthOnlineExamQuestion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/提交答案"
    url = f"/service-question/monthExamination/app/commitMonthOnlineExamQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/获取试卷答题情况")
def monthExamination_app_getQuestionResult_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/获取试卷答题情况"
    url = f"/service-question/monthExamination/app/getQuestionResult"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/分享")
def monthExamination_app_share_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/分享"
    url = f"/service-question/monthExamination/app/share"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/分享日志")
def monthExamination_app_share_log_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/分享日志"
    url = f"/service-question/monthExamination/app/share/log"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/月考/查询报告详情成绩tab页")
def monthExamination_app_report_getMonthOnlineExamReport_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/月考/查询报告详情成绩tab页"
    url = f"/service-question/monthExamination/app/report/getMonthOnlineExamReport"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

