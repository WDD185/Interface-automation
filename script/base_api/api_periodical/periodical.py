
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("管理内刊/查阅端/干部内刊列表")
def periodical_listPeriodicals_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "管理内刊/查阅端/干部内刊列表"
    url = f"/api-periodical/periodical/listPeriodicals"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊内容")
def periodical_listPeriodicalContents_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "管理内刊/查阅端/干部内刊内容"
    url = f"/api-periodical/periodical/listPeriodicalContents"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊内容免鉴权查看")
def periodical_listPeriodicalContentsNoAuth_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "管理内刊/查阅端/干部内刊内容免鉴权查看"
    url = f"/api-periodical/periodical/listPeriodicalContentsNoAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊书架")
def periodical_listPeriodicalsOnReadNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "管理内刊/查阅端/干部内刊书架"
    url = f"/api-periodical/periodical/listPeriodicalsOnReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

