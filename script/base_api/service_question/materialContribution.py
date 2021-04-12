
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极题库")
def materialContribution_updateContributionsTarget_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极题库"
    url = f"/service-question/materialContribution/updateContributionsTarget"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def materialContribution_getContributionsByDate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极题库"
    url = f"/service-question/materialContribution/getContributionsByDate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def materialContribution_getContributions_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极题库"
    url = f"/service-question/materialContribution/getContributions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/区域上传统计")
def materialContribution_getMaterialUploads_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极题库/区域上传统计"
    url = f"/service-question/materialContribution/getMaterialUploads"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

