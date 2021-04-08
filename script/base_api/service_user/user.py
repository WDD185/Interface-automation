
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/基础/用户登录(验证码)")
def user_loginOrAddByVerificationCode_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/loginOrAddByVerificationCode"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/修改密码")
def user_updatePassWord_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/updatePassWord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/修改手机号")
def user_updateUserPhone_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/updateUserPhone"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/微信绑定")
def user_bindWxMini_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/bindWxMini"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/微信登录")
def user_loginByWx_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/loginByWx"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/根据用户手机查询用户")
def user_customer_getUserByPhone_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/customer/getUserByPhone"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/在线商城/查询登录用户信息")
def user_customer_getLoginUserPhone_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/customer/getLoginUserPhone"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/用户登录(微信手机号)")
def user_loginByWxPhone_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-user/user/loginByWxPhone"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

