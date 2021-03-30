
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/文件上传/用户文件上传")
def upload_ppt_user_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/ppt/user"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/富文本图片文件上传")
def upload_richEditor_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/richEditor/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/头像上传")
def upload_file_avatar_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/file/avatar"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/一般文件上传")
def upload_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/课件库文件上传")
def upload_courseware_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/courseware/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/Base64上传")
def upload_file_base64_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/file/base64"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/图片文件上传")
def upload_homework_img_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/homework/img"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/作业/其他文件上传")
def upload_homework_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/homework/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/备课文件上传")
def upload_prepare_lesson_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/prepare_lesson/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/文件上传/多个Base64上传")
def upload_file_base64Multiple_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/file/base64Multiple"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/题库/上传")
def upload_question_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/upload/question/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/上传视频")
def upload_putVod_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_src/upload/putVod"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/上传cos")
def upload_putCos_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_src/upload/putCos"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

