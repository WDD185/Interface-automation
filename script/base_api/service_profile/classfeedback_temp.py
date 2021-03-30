
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取未读班贴数量")
def classfeedback_student_unread_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classfeedback/student/unread/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴列表")
def classfeedback_student_notes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classfeedback/student/notes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴详情")
def classfeedback_student_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classfeedback/student/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生具体某堂课的班帖详情")
def classfeedback_classId_class_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classfeedback/{classId}/class/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

