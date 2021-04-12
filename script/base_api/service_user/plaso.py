
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("伯索账密鉴权")
def plaso_auth_employee_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "伯索账密鉴权"
    url = f"/service-user/plaso/auth/employee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索钉钉扫码鉴权")
def plaso_auth_dingQR_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "伯索钉钉扫码鉴权"
    url = f"/service-user/plaso/auth/dingQR"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

