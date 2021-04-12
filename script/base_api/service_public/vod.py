
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("视频上传/签名获取")
def vod_signature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "视频上传/签名获取"
    url = f"/service-public/vod/signature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

