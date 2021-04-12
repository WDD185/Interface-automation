
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/批量转班/查询转入班级")
def batch_changeClass_classIn_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/查询转入班级"
    url = f"/service-education/batch/changeClass/classIn"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/批量转班/查询转出班级")
def batch_changeClass_classOut_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/批量转班/查询转出班级"
    url = f"/service-education/batch/changeClass/classOut"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

