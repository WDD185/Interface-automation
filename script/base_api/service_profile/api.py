
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("伯索回调")
def api_plaso_callback_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "伯索回调"
    url = f"/service-profile/api/plaso/callback"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

