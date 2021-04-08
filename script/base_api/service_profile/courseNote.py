
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户行课/获取学生用户的班帖列表所包含的属性")
def courseNote_field_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-profile/courseNote/field"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

