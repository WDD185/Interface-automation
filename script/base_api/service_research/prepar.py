
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("/教研/课件库/文件启用禁用接口")
def prepar_lessons_textbook_enable_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/enable"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/文件查阅接口")
def prepar_lessons_textbook_checkRead_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/checkRead"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/反馈接口")
def prepar_lessons_textbook_feedback_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/feedback"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/讲次和课件")
def prepar_lessons_textbook_countResource_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/countResource"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/点击查阅(未查阅)详情")
def prepar_lessons_textbook_readDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/readDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/(未查阅)详情")
def prepar_lessons_textbook_unReadDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/unReadDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/点击操作人")
def prepar_lessons_textbook_opeLog_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/opeLog"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/反馈查询")
def prepar_lessons_textbook_feedbackSelcet_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/feedbackSelcet"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/反馈详情")
def prepar_lessons_textbook_feedbackDetaill_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/feedbackDetaill"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/更新说明")
def prepar_lessons_textbook_updateLog_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/updateLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/上课/埋点导入")
def prepar_lessons_textbook_statistical_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/statistical"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/上课/埋点查询")
def prepar_lessons_textbook_queryStatistical_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/queryStatistical"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/上课/抽问导入")
def prepar_lessons_textbook_insertQuestionPerformInClass_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/insertQuestionPerformInClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/上课/抽问查询")
def prepar_lessons_textbook_queryQuestionPerformInClass_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/queryQuestionPerformInClass"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/课件库/讲次/未发送详情列表")
def prepar_lessons_textbook_notSendDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/notSendDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/课件库/讲次/已发送详情列表")
def prepar_lessons_textbook_sendDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/sendDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/课件库/添加极客资料读取日志")
def prepar_lessons_addLectureContentReadLog_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/addLectureContentReadLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/课件库/讲次/学生已读列表")
def prepar_lessons_textbook_studentReadDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/studentReadDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/课件库/讲次/讲次文件内容(免登录的)")
def prepar_lessons_textbook_lectureFiles_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/lectureFiles"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课/获取家长讲义打包下载zip的url")
def prepar_lessons_lecture_getParentalNotesDownloadUrl_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/lecture/getParentalNotesDownloadUrl"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课视频更新")
def prepar_lessons_textbook_updatePrepareVideo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/prepar/lessons/textbook/updatePrepareVideo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

