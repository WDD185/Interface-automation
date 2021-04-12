
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营PC保存分享")
def share_saveShare_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营PC保存分享"
    url = f"/api-operation-web/share/saveShare"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营查询分享业绩统计")
def share_selectShareStatistics_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营查询分享业绩统计"
    url = f"/api-operation-web/share/selectShareStatistics"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营导出分享业绩统计")
def share_shareStatisticsExport_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营导出分享业绩统计"
    url = f"/api-operation-web/share/shareStatisticsExport"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

