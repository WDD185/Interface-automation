
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("用户/钉钉/h5免密登录")
def dingAuth_h5_periodicalAuth_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/dingAuth/h5/periodicalAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教师基本功大赛/钉钉登录")
def dingAuth_h5_basicSkillAuth_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/dingAuth/h5/basicSkillAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

