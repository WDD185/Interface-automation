
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("云盘/创建一级文件夹")
def cloudDiskController_createFolder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/createFolder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/上传")
def cloudDiskController_upload_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/upload"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/创建二级文件夹")
def cloudDiskController_createSecondLevelFolder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/createSecondLevelFolder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/查询列表")
def cloudDiskController_queryList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/queryList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/查询二级文件")
def cloudDiskController_querySecondLevelList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/querySecondLevelList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/修改权限")
def cloudDiskController_editFactor_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/editFactor"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/删除")
def cloudDiskController_delete_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/delete"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/查询大区")
def cloudDiskController_queryRegionByCloudDiskId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/queryRegionByCloudDiskId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/查询详情")
def cloudDiskController_queryCloudDiskDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/queryCloudDiskDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/查询log")
def cloudDiskController_queryOperation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/queryOperation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/修改名称")
def cloudDiskController_updateFileName_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/updateFileName"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("云盘/切换是否下载")
def cloudDiskController_updateDownloadStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/cloudDiskController/updateDownloadStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

