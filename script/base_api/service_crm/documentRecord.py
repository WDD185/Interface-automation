
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("知识/知识列表/下载明细")
def documentRecord_export_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "知识/知识列表/下载明细"
    url = f"/service-crm/documentRecord/export"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/知识树/下载")
def documentRecord_operate_download_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/知识树/下载"
    url = f"/service-crm/documentRecord/operate/download"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

