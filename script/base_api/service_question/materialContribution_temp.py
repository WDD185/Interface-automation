
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极题库")
def materialContribution_updateContributionsTarget_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/materialContribution/updateContributionsTarget"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def materialContribution_getContributionsByDate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/materialContribution/getContributionsByDate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def materialContribution_getContributions_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/materialContribution/getContributions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/区域上传统计")
def materialContribution_getMaterialUploads_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/materialContribution/getMaterialUploads"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

