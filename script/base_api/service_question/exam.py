
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极教研/卷库/编辑试卷-试卷题单必填属性")
def exam_paper_filterCondition_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/filterCondition"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/手动选题创建试卷/题单")
def exam_paper_createPaper_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/createPaper"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/手动选题复制试卷/题单")
def exam_paper_copyPaper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/copyPaper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/手动选题查询试卷/题单")
def exam_paper_queryPaperList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/queryPaperList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/编辑试卷-保存试卷/题单")
def exam_paper_savePaper_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/savePaper"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/编辑试卷-试卷/题单详情查询")
def exam_paper_PaperDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/PaperDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/试卷/题单删除")
def exam_paper_deletePaper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/deletePaper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/试卷/题单上传排版文档")
def exam_paper_uploadTypeDocuments_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/uploadTypeDocuments"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/试卷/删除排版文档")
def exam_paper_delTypeDocument_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/delTypeDocument"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/试卷/题单上传排版文档查阅")
def exam_paper_getTypeDocument_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/getTypeDocument"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/卷库/文件上传")
def exam_paper_upload_file_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/upload/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("卷库试卷下载")
def exam_paper_download_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/download"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/成绩导入")
def exam_grade_import_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/grade/import"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/查询单科成绩列表")
def exam_subject_grades_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/subject/grades/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/修改学生成绩")
def exam_student_grade_modify_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/student/grade/modify"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/清空成绩")
def exam_subject_grade_clear_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/subject/grade/clear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/查询是否有正在执行的任务")
def exam_executing_task_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/executing/task/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/任务查询")
def exam_task_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/task/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/pdf报告查询")
def exam_examSubjectPdfReport_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examSubjectPdfReport/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长app/考试成绩报告/多科考试成绩报告查询")
def exam_app_examTotalReport_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examTotalReport/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长app/考试成绩报告/单科科考试成绩报告基础信息查询")
def exam_app_examSubjectBaseReport_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examSubjectBaseReport/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长app/考试成绩报告/单科考试成绩报告tab查询")
def exam_app_examSubjectReport_detail_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examSubjectReport/detail/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长app/考试成绩报告/单科科考试成绩报告基础信息查询（缺考）")
def exam_app_examSubjectBaseReport_noAttend_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examSubjectBaseReport/noAttend/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长app/考试成绩报告/单科考试成绩报告tab查询（缺考）")
def exam_app_examSubjectReport_noAttend_detail_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examSubjectReport/noAttend/detail/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/发布报告")
def exam_publishExamReport_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/publishExamReport"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告列表")
def exam_reportList_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/reportList/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/成绩报告/下载弹窗校区列表")
def exam_schoolAreaList_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/schoolAreaList/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/成绩报告/下载")
def exam_report_download_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/report/download"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/撤回考试")
def exam_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/成绩报告上传pdf")
def exam_pdf_upload_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/pdf/upload"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长App/阅读成绩报告")
def exam_app_report_read_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/report/read"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/考试基础信息查询")
def exam_examMessage_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examMessage"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/考试基础信息修改")
def exam_upExamMessage_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/upExamMessage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/新建考试")
def exam_createExam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/createExam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/导入试卷")
def exam_importQuestion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/importQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/试卷结构详情")
def exam_dataStructureQuestion_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/dataStructureQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/知识点评语获取知识点信息")
def exam_getKnowledge_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/getKnowledge"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/知识点评语保存")
def exam_knowComment_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/knowComment"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/分数评语保存")
def exam_scoreComment_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/scoreComment"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/获取分数评语详情")
def exam_getScoreComment_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/getScoreComment"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/科目信息查询")
def exam_examSubjectDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examSubjectDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/考试列表查询")
def exam_examList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/作废考试")
def exam_invalidExam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/invalidExam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/重启考试")
def exam_examRestart_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examRestart"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/删除考试")
def exam_examDel_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examDel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/删除试卷")
def exam_examQuestionDel_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examQuestionDel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/撤回考试")
def exam_examRetract_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/examRetract"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/操作日志详情")
def exam_operLog_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/operLog"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/发布时间设置")
def exam_releasePublishTime_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/releasePublishTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告/发布时间详情")
def exam_publishTimeDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/publishTimeDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/卷库/试卷列表/引用次数详情")
def exam_paper_referCountDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/referCountDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/考试/分享")
def exam_app_share_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/share"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/清除评语")
def exam_clearknowComment_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/clearknowComment"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/考试/成绩报告Excel导入")
def exam_readFile_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/readFile"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/课件库/查询学生考试记录")
def exam_query_student_id_get(id, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/query/student/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/老数据处理")
def exam_paper_transfer_question_source_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/transfer_question_source"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/删除试卷")
def exam_paper_deleteExamPaper_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/deleteExamPaper"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/复制试卷")
def exam_paper_copyExamPaper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/copyExamPaper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/保存更新试卷")
def exam_paper_saveOrUpdateExamPaper_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/saveOrUpdateExamPaper"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/创建试卷")
def exam_paper_createExamPaper_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/createExamPaper"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/查询试卷详情")
def exam_paper_queryExamPaper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/queryExamPaper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/卷库/卷库列表查询")
def exam_paper_queryExamPaperList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/queryExamPaperList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长App/查询学生考试答题结果解析")
def exam_app_examResultAnalysis_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examResultAnalysis/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长App/查询学生考试答题结果解析（缺考）")
def exam_app_examResultAnalysis_noAttend_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/app/examResultAnalysis/noAttend/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/考试/下载成绩导入模板")
def exam_grade_template_download_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/grade/template/download"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/收藏、移除收藏")
def exam_paper_paper_bookmark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/paper_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/新建收藏夹")
def exam_paper_bookmark_create_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/bookmark_create"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/个人收藏夹目录列表")
def exam_paper_bookmark_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/bookmark_list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/个人收藏试卷列表")
def exam_paper_personal_bookmark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/personal_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/30日内热门试卷列表")
def exam_paper_hot_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/hot"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/查询试卷操作日志")
def exam_paper_operation_logs_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/operation_logs"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/卷库列表")
def exam_paper_jst_queryExamPaperList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/queryExamPaperList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/30日内热门试卷列表")
def exam_paper_jst_hot_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/hot"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/查看试卷详情")
def exam_paper_jst_queryExamPaper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/queryExamPaper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/查看排版文档")
def exam_paper_jst_getTypeDocument_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/getTypeDocument"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/试卷下载")
def exam_paper_jst_download_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/download"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/收藏、移除收藏")
def exam_paper_jst_paper_bookmark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/paper_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/新建收藏夹")
def exam_paper_jst_bookmark_create_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/bookmark_create"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人收藏夹目录列表")
def exam_paper_jst_bookmark_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/bookmark_list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人收藏试卷列表")
def exam_paper_jst_personal_bookmark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/personal_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/试卷结构分析")
def exam_paper_jst_structure_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/structure"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/添加题目到试题篮")
def exam_paper_jst_add_question_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/add_question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/删除试题篮题目")
def exam_paper_jst_del_question_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/del_question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/复制试卷")
def exam_paper_jst_copyExamPaper_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/copyExamPaper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/编辑试卷保存")
def exam_paper_jst_saveOrUpdateExamPaper_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/saveOrUpdateExamPaper"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/删除试卷")
def exam_paper_jst_deleteExamPaper_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/deleteExamPaper"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/收藏、移除组卷")
def exam_paper_jst_composes_bookmark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/composes_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/新建组卷文件夹")
def exam_paper_jst_bookmark_create_composes_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/bookmark_create_composes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人组卷文件夹目录列表")
def exam_paper_jst_bookmark_list_composes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/bookmark_list_composes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/个人组卷列表")
def exam_paper_jst_personal_bookmark_composes_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/personal_bookmark_composes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/清除当前草稿")
def exam_paper_jst_clear_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/jst/clear_question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/清除当前草稿")
def exam_paper_clear_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/clear_question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/试卷结构分析")
def exam_paper_structure_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/structure"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/添加题目到试题篮")
def exam_paper_add_question_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/add_question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/删除试题篮题目")
def exam_paper_del_question_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-question/exam/paper/del_question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

