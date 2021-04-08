
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("JkyAPP/校区线索查询")
def back_clue_get_school_clues_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/get-school-clues"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/校区分配线索")
def back_clue_distribute_person_clues_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/distribute-person-clues"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询个人线索")
def back_clue_get_person_clues_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/get-person-clues"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询最后一次的跟进中的有哪些人")
def back_clue_params_query_last_clue_employees_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/params/query-last-clue-employees"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询返报线索")
def back_clue_query_by_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/query-by-id"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/查询默认校区")
def back_clue_queryDefaultAreaByEmployeeId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/queryDefaultAreaByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/设置APP默认校区")
def back_clue_saveDefaultArea_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/saveDefaultArea"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/返报线索-校区-统计")
def back_clue_school_area_schoolAreaBackClues_statistics_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/school-area-schoolAreaBackClues-statistics"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/返报线索-校区-详情")
def back_clue_school_area_schoolAreaBackClues_details_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/school-area-schoolAreaBackClues-details"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/返报线索-校区")
def back_clue_school_area_statisticsSchoolAreaBackClues_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/school-area-statisticsSchoolAreaBackClues"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/返报线索-个人")
def back_clue_personal_statisticsSchoolAreaBackClues_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/back-clue/personal-statisticsSchoolAreaBackClues"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

