
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/使用手机验证码登录")
def login_verificationCode_receiveVerificationCode_studentPhoneNum_phoneNumber_get(verificationCode, studentPhoneNum, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/使用手机验证码登录"
    url = f"/service-profile/login/{verificationCode}/receiveVerificationCode/{studentPhoneNum}/phoneNumber"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

