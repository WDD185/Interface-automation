
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题")
def feedback_mailbox_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/feedback/mailbox"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/向校长信箱反馈问题")
def feedback_mailbox_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/feedback/mailbox/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题上传的图片")
def feedback_feedbackId_mailbox_picture_get(feedbackId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/feedback/{feedbackId}/mailbox/picture"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

