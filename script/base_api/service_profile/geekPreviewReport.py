
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通/预习学情/课前预习班级列表")
def geekPreviewReport_queryAttendClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/预习学情/课前预习班级列表"
    url = f"/service-profile/geekPreviewReport/queryAttendClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/预习学情/预习内容")
def geekPreviewReport_queryPreviewContent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/预习学情/预习内容"
    url = f"/service-profile/geekPreviewReport/queryPreviewContent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/预习学情/预习情况")
def geekPreviewReport_queryPreviewSituation_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/预习学情/预习情况"
    url = f"/service-profile/geekPreviewReport/queryPreviewSituation"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/预习学情/预习详情")
def geekPreviewReport_queryPreviewDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/预习学情/预习详情"
    url = f"/service-profile/geekPreviewReport/queryPreviewDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/预习学情/历史预习详情")
def geekPreviewReport_queryHistoryPreviewDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/预习学情/历史预习详情"
    url = f"/service-profile/geekPreviewReport/queryHistoryPreviewDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学情管理/课前预习/导出预习excel")
def geekPreviewReport_exportPreviewSituation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/学情管理/课前预习/导出预习excel"
    url = f"/service-profile/geekPreviewReport/exportPreviewSituation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学情管理/课前预习/预习讲次查询")
def geekPreviewReport_queryLectureCompleteRate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/学情管理/课前预习/预习讲次查询"
    url = f"/service-profile/geekPreviewReport/queryLectureCompleteRate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

