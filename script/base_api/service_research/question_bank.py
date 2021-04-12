
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("教研/题库/word导入")
def question_bank_doc_import_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/word导入"
    url = f"/service-research/question_bank/doc/import"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/查询题目操作日志")
def question_bank_question_operation_logs_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/查询题目操作日志"
    url = f"/service-research/question_bank/question/operation_logs"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/题目筛选条件")
def question_bank_query_condition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/题目筛选条件"
    url = f"/service-research/question_bank/query_condition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/获取行政区")
def question_bank_administrative_region_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/获取行政区"
    url = f"/service-research/question_bank/administrative_region"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树查询")
def question_bank_knowledge_tree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/知识树查询"
    url = f"/service-research/question_bank/knowledge_tree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/知识点查询")
def question_bank_knowledge_tree_points_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/知识树/知识点查询"
    url = f"/service-research/question_bank/knowledge_tree/points"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/增加编辑移动")
def question_bank_knowledge_tree_points_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/知识树/增加编辑移动"
    url = f"/service-research/question_bank/knowledge_tree/points"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/删除节点")
def question_bank_knowledge_tree_point_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/知识树/删除节点"    
    url = f"/service-research/question_bank/knowledge_tree/point"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/查询列表")
def question_bank_questions_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/查询列表"
    url = f"/service-research/question_bank/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/题目详情查询")
def question_bank_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/题目详情查询"
    url = f"/service-research/question_bank/question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/新建题")
def question_bank_question_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/新建题"
    url = f"/service-research/question_bank/question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/更新编辑题")
def question_bank_question_patch(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/更新编辑题"
    url = f"/service-research/question_bank/question"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/删除题")
def question_bank_question_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "教研/题库/删除题"    
    url = f"/service-research/question_bank/question"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

