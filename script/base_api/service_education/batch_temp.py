
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/批量转班/查询转入班级")
def batch_changeClass_classIn_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/batch/changeClass/classIn"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/批量转班/查询转出班级")
def batch_changeClass_classOut_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/batch/changeClass/classOut"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

