
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/报表/学员考勤/批量补课、补点名")
def attendances_batch_update_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/batch/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/课消/查询某次课课消详情")
def attendances_queries_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/报表/学员考勤/查询考勤数据")
def attendances_reports_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/reports"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/课消/查询课消数据")
def attendances_overviews_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/overviews"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/点名/老师操作点名")
def attendances_schedules_scheduleId_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/schedules/{scheduleId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/点名/获取最大课次")
def attendances_indexs_max_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/indexs/max"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/课消/Excel导出")
def attendances_overviews_excel_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/overviews/excel"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/课消/计费")
def attendances_charge_scheduleId_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/charge/{scheduleId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/点名/班级类型查询点名类型")
def attendances_type_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/type"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/教务管理/课消/查看出勤")
def attendances_attendances_records_queries_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/attendances/attendances-records/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

