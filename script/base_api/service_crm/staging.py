
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/工作台/在读学员数据")
def staging_queryDirectorReportForStageRead_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/工作台/在读学员数据"
    url = f"/service-crm/staging/queryDirectorReportForStageRead"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/工作台/流失学员数据")
def staging_queryDirectorReportForStageRefund_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/工作台/流失学员数据"
    url = f"/service-crm/staging/queryDirectorReportForStageRefund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/班主任/单个校区-招生人次")
def staging_geek_data_person_time_count_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/班主任/单个校区-招生人次"
    url = f"/service-crm/staging/geek/data/person-time-count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/班主任/单个区域-招生人次列表")
def staging_geek_data_schools_person_time_count_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/班主任/单个区域-招生人次列表"
    url = f"/service-crm/staging/geek/data/schools-person-time-count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/CRM/班主任/单个区域-招生人次区域")
def staging_geek_get_areas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/CRM/班主任/单个区域-招生人次区域"
    url = f"/service-crm/staging/geek/get-areas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("CRM/工作台/提成人次")
def staging_geek_data_commissionPersonTimeCount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "CRM/工作台/提成人次"
    url = f"/service-crm/staging/geek/data/commissionPersonTimeCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("CRM/工作台/校区提成人次")
def staging_geek_data_schoolCommissionPersonTimeCount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "CRM/工作台/校区提成人次"
    url = f"/service-crm/staging/geek/data/schoolCommissionPersonTimeCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

