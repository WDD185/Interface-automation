
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮App/双师/查看校区配置")
def playVideo_querySchoolConfig_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮App/双师/查看校区配置"
    url = f"/api-jksxb-app/playVideo/querySchoolConfig"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

