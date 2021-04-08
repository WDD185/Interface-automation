
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("寒假备课/审核教材列表")
def examine_findExamineTextbooksList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/findExamineTextbooksList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/教材讲次审核列表")
def examine_findExamineLectureList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/findExamineLectureList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("寒假备课/审核成员列表")
def examine_findExamineMemberList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/findExamineMemberList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审核/教师查询筛选")
def examine_findAllExamineMember_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/findAllExamineMember"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审核/教材权限开关接口")
def examine_manageTextbooks_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/manageTextbooks"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/备课审核/教学组织架构树获取")
def examine_queryDepartment_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/queryDepartment"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的视频/视频分享获取班级")
def examine_queryClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/queryClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/备课大厅/教材/备课进度")
def examine_getPreparingStep_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/getPreparingStep"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的视频/视频分享获取学生")
def examine_getStudentInfoByClassId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/getStudentInfoByClassId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/我的视频/视频分享接口")
def examine_videoShare_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-descartes/examine/videoShare"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

