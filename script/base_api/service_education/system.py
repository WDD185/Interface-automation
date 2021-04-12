
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/课程类型设置,教学参数设置/查询")
def system_setting_query_param_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/课程类型设置,教学参数设置/查询"
    url = f"/service-education/system/setting/query/param"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/课程类型设置,教学参数设置/修改")
def system_setting_update_param_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/课程类型设置,教学参数设置/修改"
    url = f"/service-education/system/setting/update/param"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置,学生身份/修改")
def system_setting_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置,学生身份/修改"
    url = f"/service-education/system/setting/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置,学生身份/删除")
def system_setting_del_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置,学生身份/删除"    
    url = f"/service-education/system/setting/del"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置,学生身份/增加")
def system_setting_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置,学生身份/增加"
    url = f"/service-education/system/setting/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置,学生身份/查询")
def system_setting_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置,学生身份/查询"
    url = f"/service-education/system/setting/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/课程类型设置/新增班级类型")
def system_setting_add_param_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/课程类型设置/新增班级类型"
    url = f"/service-education/system/setting/add/param"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/全参数查询")
def system_setting_query_all_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/全参数查询"
    url = f"/service-education/system/setting/query/all"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/更新校区")
def system_setting_update_campus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/更新校区"
    url = f"/service-education/system/setting/update/campus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/查询班级类型")
def system_productCourseType_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/查询班级类型"
    url = f"/service-education/system/productCourseType"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/退费动态参数新增")
def system_setting_addSettingByParam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/退费动态参数新增"
    url = f"/service-education/system/setting/addSettingByParam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/退费动态参数修改")
def system_setting_editSettingByParam_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/退费动态参数修改"
    url = f"/service-education/system/setting/editSettingByParam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/查询退费原因列表")
def system_setting_querySystemSettings_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/查询退费原因列表"
    url = f"/service-education/system/setting/querySystemSettings"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/极运营/退费/查询退费原因")
def system_setting_queryGeneralSettings_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/极运营/退费/查询退费原因"
    url = f"/service-education/system/setting/queryGeneralSettings"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/查询年级")
def system_queryGrades_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/查询年级"
    url = f"/service-education/system/queryGrades"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

