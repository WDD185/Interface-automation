
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("在线考试/参加考试")
def examination_app_join_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/join"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/查询报告列表")
def examination_app_reports_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/reports/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/查询报告基础信息")
def examination_app_report_base_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/report/base/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/报告详情tab页查询")
def examination_app_report_detail_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/report/detail/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/学生获取单个考试详情")
def examination_app_queryExaminationDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/queryExaminationDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/成绩报告小红点")
def examination_app_report_unread_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/report/unread/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/生成成绩报告")
def examination_app_generate_report_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/generate/report"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/查询学生考试记录状态")
def examination_app_recordStatus_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/recordStatus/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/学情")
def examination_pc_studyRes_examId_classId_get(examId, classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/pc/studyRes/{examId}/{classId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/获取系统时间")
def examination_app_systemTime_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/systemTime"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/app考试列表")
def examination_app_queryExamination_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/queryExamination"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/pc查询班级考试列表")
def examination_pc_queryExams_classId_get(classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/pc/queryExams/{classId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/app交卷")
def examination_app_answerQuestions_examPaperId_examId_studentId_post(examPaperId, examId, studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/answerQuestions/{examPaperId}/{examId}/{studentId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/答题")
def examination_app_getQuestions_examPaperId_get(examPaperId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/getQuestions/{examPaperId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/答题解析")
def examination_app_getQuestionResult_examId_get(examId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/getQuestionResult/{examId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/学情导出")
def examination_pc_ExportStudyRes_examId_classId_get(examId, classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/pc/ExportStudyRes/{examId}/{classId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/分享")
def examination_app_share_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/share"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/数据导入")
def examination_app_importData_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/importData"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/在线考试/补考分享链接")
def examination_pc_makeup_exam_url_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/pc/makeup/exam/url"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/在线考试/根据链接获取学生token")
def examination_pc_makeup_url_msg_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/pc/makeup/url/msg"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/导入考试数据")
def examination_app_readFile_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/readFile"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/在线考试/分享/日志")
def examination_app_share_log_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/share/log"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/查询报告基础信息（缺考）")
def examination_app_report_base_noAttend_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/report/base/noAttend/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线考试/报告详情tab页查询（缺考）")
def examination_app_report_detail_noAttend_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/report/detail/noAttend/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端app/在线考试/学生查阅报告日志")
def examination_app_report_base_read_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/examination/app/report/base/read"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

