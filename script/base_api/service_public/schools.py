
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/前台业务/报名/新增学生/就读学校名查询")
def schools_queryCanUse_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/前台业务/报名/新增学生/就读学校名查询"
    url = f"/service-public/schools/queryCanUse"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/公立学校/新增")
def schools_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/公立学校/新增"
    url = f"/service-public/schools/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/公立学校/编辑")
def schools_edit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/公立学校/编辑"
    url = f"/service-public/schools/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/公立学校/查询列表")
def schools_queryAll_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/公立学校/查询列表"
    url = f"/service-public/schools/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础参数设置/公立学校/编辑状态")
def schools_updateStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础参数设置/公立学校/编辑状态"
    url = f"/service-public/schools/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础设置/全日制学校导出")
def schools_export_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础设置/全日制学校导出"
    url = f"/service-public/schools/export"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础设置/全日制学校详情")
def schools_detail_id_get(id, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础设置/全日制学校详情"
    url = f"/service-public/schools/detail/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础设置/全日制学校年级列表")
def schools_grades_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础设置/全日制学校年级列表"
    url = f"/service-public/schools/grades"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础设置/全日制学校年级修改")
def schools_grades_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础设置/全日制学校年级修改"
    url = f"/service-public/schools/grades/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/基础设置/全日制学校年级导出")
def schools_grades_export_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/基础设置/全日制学校年级导出"
    url = f"/service-public/schools/grades/export"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

