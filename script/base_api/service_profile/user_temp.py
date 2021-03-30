
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码")
def user_studentId_backupMobilePhone_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/user/{studentId}/backupMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码")
def user_studentId_bindingMobilePhone_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/user/{studentId}/bindingMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录密码")
def user_type_signInPassword_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/user/{type}/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/用户登录(验证码)")
def user_loginOrAddByVerificationCode_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/loginOrAddByVerificationCode"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/修改密码")
def user_updatePassWord_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/updatePassWord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/修改手机号")
def user_updateUserPhone_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/updateUserPhone"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/微信绑定")
def user_bindWxMini_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/bindWxMini"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/微信登录")
def user_loginByWx_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/loginByWx"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/根据用户手机查询用户")
def user_customer_getUserByPhone_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/customer/getUserByPhone"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/在线商城/查询登录用户信息")
def user_customer_getLoginUserPhone_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/customer/getLoginUserPhone"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/基础/用户登录(微信手机号)")
def user_loginByWxPhone_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/user/loginByWxPhone"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/获取游客ID")
def user_visitor_generateId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/user/visitor/generateId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/绑定游客与学生")
def user_visitor_bindUser_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/user/visitor/bindUser"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/活动商品下单")
def user_goods_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/user/goods/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/绑定活动商品码")
def user_goods_bindCode_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/user/goods/bindCode"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/学生购买商品查询")
def user_goods_list_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/user/goods/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/学生地理位置记录")
def user_address_addOrUpdate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/user/address/addOrUpdate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

