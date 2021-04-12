
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/班主任机制/工作台/根据员工ID批量修改")
def workbench_menu_update_batch_employeeId_post(employeeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任机制/工作台/根据员工ID批量修改"
    url = f"/service-user/workbench/menu/update/batch/{employeeId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/班主任机制/工作台/根据员工ID查询")
def workbench_menu_employeeId_post(employeeId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/班主任机制/工作台/根据员工ID查询"
    url = f"/service-user/workbench/menu/{employeeId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

