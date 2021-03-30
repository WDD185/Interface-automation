
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("干部内刊列表")
def periodical_listPeriodicals_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/periodical/listPeriodicals"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("干部内刊内容")
def periodical_listPeriodicalContents_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/periodical/listPeriodicalContents"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊列表")
def periodical_listPeriodicals_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodical/listPeriodicals"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊内容")
def periodical_listPeriodicalContents_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodical/listPeriodicalContents"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊内容免鉴权查看")
def periodical_listPeriodicalContentsNoAuth_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodical/listPeriodicalContentsNoAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("管理内刊/查阅端/干部内刊书架")
def periodical_listPeriodicalsOnReadNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_periodical/periodical/listPeriodicalsOnReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

