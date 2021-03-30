
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/课表/查询班级排课")
def schedules_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/schedules"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

