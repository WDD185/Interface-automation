
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/考试/获取学生在线产品考试列表")
def productExamination_app_getProductOnlineExamAppList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/getProductOnlineExamAppList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/根据考试id获取考试信息")
def productExamination_app_getProductOnlineExamInfoApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/getProductOnlineExamInfoApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/根据考试id获取试卷详情")
def productExamination_app_getProductOnlineExamPaperInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/getProductOnlineExamPaperInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/参加考试")
def productExamination_app_attendProductExam_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/attendProductExam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/提交答案")
def productExamination_app_commitProductOnlineExamQuestion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/commitProductOnlineExamQuestion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/获取试卷答题情况")
def productExamination_app_getQuestionResult_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/getQuestionResult"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/分享")
def productExamination_app_share_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/share"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/分享日志")
def productExamination_app_share_log_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/share/log"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/查询报告详情tab页")
def productExamination_app_report_getProductOnlineExamReport_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/report/getProductOnlineExamReport"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/考试/返回榜单列表")
def productExamination_app_getProductExamHeroPanel_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/productExamination/app/getProductExamHeroPanel"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

