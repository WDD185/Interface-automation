
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("/教研/课件库/app段查询绑定教材")
def jst_app_research_update_getVersionNameByTeacherIdToHomeWork_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/update/getVersionNameByTeacherIdToHomeWork"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/教研/课件库/讲次查询")
def jst_app_research_textbook_courseContent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/textbook/courseContent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/教研/课件库/讲次和课件")
def jst_app_research_textbook_getCoursewareList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/textbook/getCoursewareList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/我的教材")
def jst_app_research_update_getVersionNameByTeacherId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/update/getVersionNameByTeacherId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/讲次下课件")
def jst_app_research_textbook_courseware_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/textbook/courseware"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/讲次下总数及阅读数")
def jst_app_research_lectureFileReadStat_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/lectureFileReadStat"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/我的教案列表查询")
def jst_app_research_textbook_lessonPlans_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/textbook/lessonPlans"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/教案上传")
def jst_app_research_teaching_plan_submit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/teaching_plan/submit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/查阅")
def jst_app_research_textbook_checkRead_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/textbook/checkRead"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/根据讲次查询教案")
def jst_app_research_teaching_plan_current_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/teaching_plan/current/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/教案撤回")
def jst_app_research_teaching_plan_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/teaching_plan/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/教案删除")
def jst_app_research_teaching_plan_del_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-research/jst-app/research/teaching_plan/del"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

