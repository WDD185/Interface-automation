
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/营销中心/文件上传")
def gos_upload_uploadGoods_file_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/文件上传"
    url = f"/service-gos/gos/upload/uploadGoods/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/gos/文件上传")
def gos_upload_file_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/gos/文件上传"
    url = f"/service-gos/gos/upload/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

