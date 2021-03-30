
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("教研/题库/保存视频")
def question_video_uploadVideo_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_video/uploadVideo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/删除视频")
def question_video_delete_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_video/delete"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/修改视频名称")
def question_video_updateNameById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_video/updateNameById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/课件/根据questionId获取视频列表")
def question_video_queryVideoByQuestionId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_video/queryVideoByQuestionId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/批量关联视频文件")
def question_video_uploadVideos_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_video/uploadVideos"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

