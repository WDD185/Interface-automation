
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("线上商城/小程序/支付活动商品")
def idea_pay_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/idea/pay"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/预生成shareId")
def idea_share_preCreateShareIds_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/idea/share/preCreateShareIds"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/保存分享")
def idea_share_saveShare_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/idea/share/saveShare"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/获取分享明细并记录浏览日志")
def idea_share_getShareDetailAndRecordBrowse_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/idea/share/getShareDetailAndRecordBrowse"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/分享转化排行榜")
def idea_share_getShareConvertRank_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/idea/share/getShareConvertRank"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商城/小程序/分享转化查询")
def idea_share_getShareConvertList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/idea/share/getShareConvertList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

