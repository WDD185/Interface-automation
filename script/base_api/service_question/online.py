
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("教研/在线作业/极师通APP获取班级列表")
def online_homework_getOnlineHomeworkClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/在线作业/极师通APP获取班级列表"
    url = f"/service-question/online/homework/getOnlineHomeworkClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/在线作业/极师通APP通过班级id获取课次信息")
def online_homework_getClassScheduleByClassId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/在线作业/极师通APP通过班级id获取课次信息"
    url = f"/service-question/online/homework/getClassScheduleByClassId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/在线作业/极师通APP根据班级id，课次id获取学生名单")
def online_homework_getStudentInfoByClassIdAndClassScheduleId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/在线作业/极师通APP根据班级id，课次id获取学生名单"
    url = f"/service-question/online/homework/getStudentInfoByClassIdAndClassScheduleId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/获取学生作业信息")
def online_homework_getHomeworkStudentScheduleInfo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/获取学生作业信息"
    url = f"/service-question/online/homework/getHomeworkStudentScheduleInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/保存学生确认后的答题信息")
def online_homework_confirmOnlineHomeworkImageInfo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/保存学生确认后的答题信息"
    url = f"/service-question/online/homework/confirmOnlineHomeworkImageInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/获取老师对应班级待批阅作业的学生列表")
def online_homework_getUnCorrectHomeworkStudentInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/获取老师对应班级待批阅作业的学生列表"
    url = f"/service-question/online/homework/getUnCorrectHomeworkStudentInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/获取班级讲次对应未提交，已提交，已批阅列表")
def online_homework_getHomeworkStudentRecordByStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/获取班级讲次对应未提交，已提交，已批阅列表"
    url = f"/service-question/online/homework/getHomeworkStudentRecordByStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/学生拍照上传")
def online_homework_addHomeworkStudentUploadPage_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/学生拍照上传"
    url = f"/service-question/online/homework/addHomeworkStudentUploadPage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/更新学生作业记录")
def online_homework_modHomeworkStudentRecord_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/更新学生作业记录"
    url = f"/service-question/online/homework/modHomeworkStudentRecord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/获取班级课次对应的作业页数")
def online_homework_getHomeworkStudentUploadPageNumber_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/获取班级课次对应的作业页数"
    url = f"/service-question/online/homework/getHomeworkStudentUploadPageNumber"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/老师批注作业正误")
def online_homework_correctHomeworkWhetherRight_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/老师批注作业正误"
    url = f"/service-question/online/homework/correctHomeworkWhetherRight"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库/在线作业/老师批注作业")
def online_homework_correctHomeworkAnalyse_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "题库/在线作业/老师批注作业"
    url = f"/service-question/online/homework/correctHomeworkAnalyse"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

