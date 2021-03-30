
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("寒假备课/获取讲次列表")
def lessons_findLectureList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findLectureList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/获取tab页未完成数量")
def lessons_findLectureTab_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findLectureTab"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/获取教案视频课件列表")
def lessons_findLectureContentList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findLectureContentList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/备课查阅")
def lessons_consult_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/consult"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/我的教案")
def lessons_findMyTeachingPlan_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findMyTeachingPlan"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/上传教案")
def lessons_uploadTeachingPlan_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/uploadTeachingPlan"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/提交审核")
def lessons_applicationSubmitByTeachingPlan_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/applicationSubmitByTeachingPlan"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/审核通过")
def lessons_applicationPass_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/applicationPass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/审核不通过")
def lessons_applicationFail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/applicationFail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/撤回")
def lessons_applicationWithdraw_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/applicationWithdraw"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/删除教案")
def lessons_deleteResourcesById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/deleteResourcesById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/优秀教案列表")
def lessons_findExcellentTeachingPlanList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findExcellentTeachingPlanList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/优秀教案详细列表")
def lessons_findExcellentTeachingPlanDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findExcellentTeachingPlanDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/视频审核")
def lessons_uploadVideo_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/uploadVideo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/查询审核详情")
def lessons_findApplicationDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findApplicationDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/查询极客资料本讲预习")
def lessons_findPreviewOfThisLectureList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findPreviewOfThisLectureList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/查询极客资料")
def lessons_findMaterial_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findMaterial"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/我的视频")
def lessons_findMyVideo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_descartes/lessons/findMyVideo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

