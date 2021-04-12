
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("资源中心/上传视频")
def upload_putVod_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "资源中心/上传视频"
    url = f"/service-src/upload/putVod"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/上传cos")
def upload_putCos_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "资源中心/上传cos"
    url = f"/service-src/upload/putCos"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

