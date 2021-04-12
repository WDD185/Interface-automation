
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通/上课/班级教材查询")
def attendClass_textbook_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通/上课/班级教材查询"
    url = f"/service-research/attendClass/textbook"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

