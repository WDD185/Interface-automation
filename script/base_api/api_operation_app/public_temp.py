
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/获取系统时间")
def public_systemCurrentTime_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/public/systemCurrentTime"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询行政区域")
def public_queryAdministrativeArea_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/queryAdministrativeArea"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询行政区域--树状结构")
def public_queryAreaTree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/queryAreaTree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/就读学校名查询")
def public_schools_queryCanUse_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/schools/queryCanUse"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/上传图片--base64")
def public_file_base64Multiple_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/file/base64Multiple"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/上传图片--普通上传")
def public_file_multiple_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/file/multiple"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询所有设置")
def public_setting_query_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/setting/query/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/目标方案/查询-过滤2019寒之前")
def public_get_target_plans_split_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/get/target-plans-split"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/目标方案/查询")
def public_get_target_plans_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/public/get/target-plans"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

