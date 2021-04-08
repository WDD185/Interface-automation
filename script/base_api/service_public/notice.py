
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/消息通知/我也不知道是啥")
def notice_studentId_student_noticeId_noticeId_get(studentId, noticeId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{studentId}/student/{noticeId}/noticeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/发送通知")
def notice_noticeTypeId_post(noticeTypeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{noticeTypeId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/查询接收者消息类别")
def notice_belong_studentId_student_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/belong/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/通过类别获取消息")
def notice_studentId_student_noticeTypeId_noticeType_get(studentId, noticeTypeId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{studentId}/student/{noticeTypeId}/noticeType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/查询接收者某类消息")
def notice_belongId_belong_studentId_student_get(belongId, studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{belongId}/belong/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/查询消息阅读状态")
def notice_student_studentId_readingState_put(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):    
    url = host + f"/service-public/notice/student/{studentId}/readingState"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/消息详情")
def notice_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/获取某人的某类消息")
def notice_studentId_student_noticeTypeId_noticeType_count_get(studentId, noticeTypeId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{studentId}/student/{noticeTypeId}/noticeType/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/白名单")
def notice_whiteList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/whiteList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/查询学生的未读消息数量")
def notice_studentId_student_countOfNoticeType_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{studentId}/student/countOfNoticeType"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/通过接收者ID获取消息")
def notice_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/消息通知/查询某人的消息数量")
def notice_studentId_student_count_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/{studentId}/student/count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页/消息该状态")
def notice_change_status_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/change/status"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页/系统消息未读个数")
def notice_unReadNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/notice/unReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

