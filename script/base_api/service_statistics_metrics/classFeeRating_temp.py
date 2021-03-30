
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极数据/查询课时费评级")
def classFeeRating_queryRating_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/classFeeRating/queryRating"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询课时费")
def classFeeRating_queryClassFeeRating_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/classFeeRating/queryClassFeeRating"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/修改课时费评级")
def classFeeRating_updateRating_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/classFeeRating/updateRating"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/查询带班量和额外课时量详情")
def classFeeRating_queryClassAndDurationDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/classFeeRating/queryClassAndDurationDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/验证用户密码")
def classFeeRating_authByPassWord_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics_metrics/classFeeRating/authByPassWord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

