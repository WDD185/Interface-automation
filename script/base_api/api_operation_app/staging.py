
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营APP/数据/个人招生人次")
def staging_geek_data_person_time_count_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/staging/geek/data/person-time-count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/校区招生人次")
def staging_geek_data_schools_person_time_count_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/staging/geek/data/schools-person-time-count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/课程顾问提成人次")
def staging_geek_data_commissionPersonTimeCount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/staging/geek/data/commissionPersonTimeCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/校区提成人次")
def staging_geek_data_schoolCommissionPersonTimeCount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/staging/geek/data/schoolCommissionPersonTimeCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/上课班级概览")
def staging_education_classes_workbench_director_classes_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/staging/education/classes/workbench/director/classes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP/数据/查询沟通记录")
def staging_geek_data_queryDirectorReportForStageRead_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-operation-app/staging/geek/data/queryDirectorReportForStageRead"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

