
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极教研web/在线作业/查询题目")
def homework_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研web/在线作业/查询题目"
    url = f"/api-research-web/homework/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/在线作业/新增题目")
def homework_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研web/在线作业/新增题目"
    url = f"/api-research-web/homework/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研web/在线作业/删除题目")
def homework_del_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极教研web/在线作业/删除题目"
    url = f"/api-research-web/homework/del"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

