
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/课程/课程清除教材")
def examination_pc_makeup_url_msg_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/课程/课程清除教材"
    url = f"/service-research/examination/pc/makeup/url/msg"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

