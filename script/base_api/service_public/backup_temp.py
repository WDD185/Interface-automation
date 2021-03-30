
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("运维配置/更新配置文件")
def backup_uploadConfig_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/backup/uploadConfig"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("运维配置/配置信息查询")
def backup_queryPreConfig_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/backup/queryPreConfig"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("运维配置/配置版本回滚")
def backup_rollback_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/backup/rollback"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("运维配置/获取停服信息")
def backup_getServerInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/backup/getServerInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("运维配置/更新停服信息")
def backup_updateServerInfo_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/backup/updateServerInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

