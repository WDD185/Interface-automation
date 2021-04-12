
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱反馈问题的反馈类型")
def feedbackType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取校长信箱反馈问题的反馈类型"
    url = f"/service-profile/feedbackType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

