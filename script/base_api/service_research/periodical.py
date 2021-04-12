
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("干部内刊列表")
def periodical_listPeriodicals_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "干部内刊列表"
    url = f"/service-research/periodical/listPeriodicals"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("干部内刊内容")
def periodical_listPeriodicalContents_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "干部内刊内容"
    url = f"/service-research/periodical/listPeriodicalContents"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

