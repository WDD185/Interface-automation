
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通/学员个人页/成绩报告列表")
def jst_exam_queryStudentReports_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/学员个人页/成绩报告列表"
    url = f"/service-question/jst/exam/queryStudentReports"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学情下载成绩报告")
def jst_exam_downloadReport_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/学情下载成绩报告"
    url = f"/service-question/jst/exam/downloadReport"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学情下载成绩excel")
def jst_exam_downloadGradeExcel_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/学情下载成绩excel"
    url = f"/service-question/jst/exam/downloadGradeExcel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/考试/学情/学期考试")
def jst_exam_examList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/考试/学情/学期考试"
    url = f"/service-question/jst/exam/examList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/考试/学情/学期考试学生详情")
def jst_exam_classExamDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/考试/学情/学期考试学生详情"
    url = f"/service-question/jst/exam/classExamDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

