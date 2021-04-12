
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/人事管理/员工信息/批量导入/下载模板")
def batchEmp_downModel_emp_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/员工信息/批量导入/下载模板"
    url = f"/service-user/batchEmp/downModel/emp"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/人事管理/员工信息/批量导入/上传文件导入")
def batchEmp_createEmp_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/人事管理/员工信息/批量导入/上传文件导入"
    url = f"/service-user/batchEmp/createEmp"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

