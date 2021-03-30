
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/获取手机号码登录验证码")
def external_login_phoneNumber_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/external/login/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/校验手机验证码")
def external_phoneNumber_validity_verificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/external/{phoneNumber}/validity/verificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取手机验证码")
def external_phoneNumber_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/external/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

