
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/作业/作业图片上传")
def app_upload_homework_img_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/upload/homework/img"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业附件上传")
def app_upload_homework_file_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/upload/homework/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/资源/App根据视频主键查询视频真实地址")
def app_src_getSrcInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/src/getSrcInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/文件上传/头像上传")
def app_file_avatar_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/file/avatar"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/通过类别获取消息")
def app_notice_studentId_student_noticeTypeId_noticeType_get(studentId, noticeTypeId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/{studentId}/student/{noticeTypeId}/noticeType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询接收者某类消息")
def app_notice_belongId_belong_studentId_student_get(belongId, studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/{belongId}/belong/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/文件上传/Base64上传")
def app_file_base64_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/file/base64"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询接收者消息类别")
def app_notice_belong_studentId_student_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/belong/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询某人的消息数量")
def app_notice_studentId_student_count_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/{studentId}/student/count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询消息阅读状态")
def app_notice_student_studentId_readingState_put(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):    
    url = host + f"/service-public/app/notice/student/{studentId}/readingState"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端APP公共功能/获取当前时间")
def app_getTimestamp_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/getTimestamp"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/系统消息")
def app_notice_change_status_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/change/status"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/未读条数")
def app_notice_unReadNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/unReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("未读消息条数")
def app_notice_countUnread_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/countUnread"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("消息设置为已读")
def app_notice_readNotice_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/readNotice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索--最近10分钟上课")
def app_notice_tenMin_send_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/app/notice/tenMin/send"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

