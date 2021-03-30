
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("通用/基础/钉钉登录")
def login_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/login"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/使用手机验证码登录")
def login_verificationCode_receiveVerificationCode_studentPhoneNum_phoneNumber_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/login/{verificationCode}/receiveVerificationCode/{studentPhoneNum}/phoneNumber"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

