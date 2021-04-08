
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极教研web/课程预习/查询课程预习")
def coursePreview_getCoursePreview_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-research-web/coursePreview/getCoursePreview"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/课程预习/保存课程预习")
def coursePreview_saveCoursePreview_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-research-web/coursePreview/saveCoursePreview"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/课程预习/获取课件的资料列表")
def coursePreview_getCoursePreviewData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-research-web/coursePreview/getCoursePreviewData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

