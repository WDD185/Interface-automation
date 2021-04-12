
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极教研")
def video_getlist_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/getlist"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_modVideoFilename_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/modVideoFilename"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_modVideoCoverImage_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/modVideoCoverImage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_reduceRelationCount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/reduceRelationCount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_queryByIdList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/queryByIdList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_queryVideoOperationLog_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/queryVideoOperationLog"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_enable_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/enable"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_del_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"    
    url = f"/service-research/video/del"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_modPlayCount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/modPlayCount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_queryVideoRelationLog_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/queryVideoRelationLog"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_VideoBindLectureContents_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/VideoBindLectureContents"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_queryVideoAlreadyBindLectures_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/queryVideoAlreadyBindLectures"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_modPlayCount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/modPlayCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研")
def video_modVideoProperty_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研"
    url = f"/service-research/video/modVideoProperty"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("视频中心/新增视频")
def video_bigFile_fileAdd_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "视频中心/新增视频"
    url = f"/service-research/video/bigFile/fileAdd"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

