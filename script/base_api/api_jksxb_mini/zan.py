
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("在线产品试验/点赞")
def zan_zan_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/点赞"
    url = f"/api-jksxb-mini/zan/zan"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线产品试验/点赞排行榜")
def zan_getLeaderboard_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/点赞排行榜"
    url = f"/api-jksxb-mini/zan/getLeaderboard"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线产品试验/查询用户当天是否点赞")
def zan_isZan_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/查询用户当天是否点赞"
    url = f"/api-jksxb-mini/zan/isZan"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线产品试验/上传拼魔方作品")
def zan_upload_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/上传拼魔方作品"
    url = f"/api-jksxb-mini/zan/upload"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线产品试验/上传文件")
def zan_upload_file_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/上传文件"
    url = f"/api-jksxb-mini/zan/upload/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线产品试验/获取个人排行")
def zan_getSelfRank_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/获取个人排行"
    url = f"/api-jksxb-mini/zan/getSelfRank"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("在线产品试验/获取拼魔方作品")
def zan_getMagicCube_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "在线产品试验/获取拼魔方作品"
    url = f"/api-jksxb-mini/zan/getMagicCube"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

