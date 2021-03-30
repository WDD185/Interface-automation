
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("教研/题库/word导入")
def question_bank_doc_import_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/doc/import"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/查询题目操作日志")
def question_bank_question_operation_logs_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/question/operation_logs"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/题目筛选条件")
def question_bank_query_condition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/query_condition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/获取行政区")
def question_bank_administrative_region_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/administrative_region"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树查询")
def question_bank_knowledge_tree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/knowledge_tree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/知识点查询")
def question_bank_knowledge_tree_points_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/knowledge_tree/points"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/增加编辑移动")
def question_bank_knowledge_tree_points_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/knowledge_tree/points"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/删除节点")
def question_bank_knowledge_tree_point_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/knowledge_tree/point"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/查询列表")
def question_bank_questions_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/题目详情查询")
def question_bank_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/新建题")
def question_bank_question_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/更新编辑题")
def question_bank_question_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/question"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/删除题")
def question_bank_question_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/question_bank/question"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极教研/题库/word导入预览")
def question_bank_doc_import_preview_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/doc/import/preview"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/题目筛选条件")
def question_bank_query_condition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/query_condition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/获取行政区")
def question_bank_administrative_region_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/administrative_region"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树查询")
def question_bank_knowledge_tree_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/knowledge_tree"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/知识点查询")
def question_bank_knowledge_tree_points_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/knowledge_tree/points"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/增加编辑移动")
def question_bank_knowledge_tree_points_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/knowledge_tree/points"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/知识树/删除节点")
def question_bank_knowledge_tree_point_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/knowledge_tree/point"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/查询列表")
def question_bank_questions_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/questions"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/题目详情查询")
def question_bank_question_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/新建题")
def question_bank_question_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/更新编辑题")
def question_bank_question_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/删除题")
def question_bank_question_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/word导入")
def question_bank_doc_import_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/doc/import"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/批量查询题目")
def question_bank_questionlist_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/questionlist"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/批量入正式库")
def question_bank_batch_warehousing_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/batch/warehousing"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("教研/题库/查询题目操作日志")
def question_bank_question_operation_logs_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question/operation_logs"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库获取导入任务结果")
def question_bank_getQuestionTaskResult_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/getQuestionTaskResult"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库单题下载")
def question_bank_download_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/download"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/题库/老数据处理")
def question_bank_transfer_question_source_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/transfer_question_source"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("题库导入任务结果入库")
def question_bank_acceptQuestionTaskResult_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/acceptQuestionTaskResult"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/待处理纠错题目列表")
def question_bank_pending_rectify_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/pending_rectify"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/题目纠错列表")
def question_bank_question_rectify_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question_rectify"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/处理纠错")
def question_bank_handle_rectify_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/handle_rectify"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/个人处理纠错题目列表")
def question_bank_question_rectified_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question_rectified"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/个人收藏题目列表")
def question_bank_personal_bookmark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/personal_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/收藏、移除收藏")
def question_bank_question_bookmark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/question_bookmark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/新建收藏夹")
def question_bank_bookmark_create_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/bookmark_create"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/删除收藏夹")
def question_bank_bookmark_delete_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/bookmark_delete"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/修改收藏夹")
def question_bank_bookmark_update_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/bookmark_update"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/移动收藏夹")
def question_bank_bookmark_move_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/bookmark_move"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/个人收藏夹目录列表")
def question_bank_bookmark_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/question_bank/bookmark_list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

