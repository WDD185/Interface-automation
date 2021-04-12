
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/招生管理/线索/导出轮巡返回url")
def export_queryUrl_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/招生管理/线索/导出轮巡返回url"
    url = f"/service-public/export/queryUrl"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

