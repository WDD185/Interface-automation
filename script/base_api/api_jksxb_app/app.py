
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮app/所有消息未读数")
def app_notice_getNotReadCount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮app/所有消息未读数"
    url = f"/api-jksxb-app/app/notice/getNotReadCount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

