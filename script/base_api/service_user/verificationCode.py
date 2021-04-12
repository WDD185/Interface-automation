
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("小程序/基础/发送短信验证码")
def verificationCode_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/基础/发送短信验证码"
    url = f"/service-user/verificationCode/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/首页/用户发送验证码")
def verificationCode_receiveVerificationCode_customer_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/首页/用户发送验证码"
    url = f"/service-user/verificationCode/receiveVerificationCode/customer"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

