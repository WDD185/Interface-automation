
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("公共/获取前端上传令牌")
def cos_getCredential_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "公共/获取前端上传令牌"
    url = f"/service-public/cos/getCredential"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

