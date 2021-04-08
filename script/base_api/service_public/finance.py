
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/财务目标设置/财务目标设置新增")
def finance_targets_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置修改")
def finance_targets_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置删除")
def finance_targets_del_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/del"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置查询全部")
def finance_targets_queryAll_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/queryAll"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置设置默认")
def finance_targets_setDefault_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/setDefault"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置设置排序")
def finance_targets_updateOrderNums_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/updateOrderNums"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细新增")
def finance_targets_add_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/add/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细修改")
def finance_targets_update_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/update/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细删除")
def finance_targets_del_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/del/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细查询全部")
def finance_targets_query_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/query/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细导出")
def finance_targets_export_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/export/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细下载模板")
def finance_targets_import_downModel_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/import/downModel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细导入模板")
def finance_targets_import_uploadModel_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-public/finance/targets/import/uploadModel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

