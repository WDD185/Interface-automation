
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/营销/营销广告/广告位设置/广告位查询")
def banner_resource_select_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告位设置/广告位查询"
    url = f"/api-operation-web/banner/resource/select"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告位设置/广告位更新")
def banner_resource_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告位设置/广告位更新"
    url = f"/api-operation-web/banner/resource/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/区域广告管理/广告位新增")
def banner_area_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/区域广告管理/广告位新增"
    url = f"/api-operation-web/banner/area/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/区域广告管理/广告位查询")
def banner_area_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/区域广告管理/广告位查询"
    url = f"/api-operation-web/banner/area/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/区域广告管理/广告位更新")
def banner_area_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/区域广告管理/广告位更新"
    url = f"/api-operation-web/banner/area/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/区域广告管理/广告位删除")
def banner_area_delete_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/区域广告管理/广告位删除"
    url = f"/api-operation-web/banner/area/delete"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/区域广告管理/广告位状态修改")
def banner_area_changeStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/区域广告管理/广告位状态修改"
    url = f"/api-operation-web/banner/area/changeStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/区域广告管理/预览")
def banner_area_display_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/区域广告管理/预览"
    url = f"/api-operation-web/banner/area/display"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/公司广告管理/广告位新增")
def banner_org_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/公司广告管理/广告位新增"
    url = f"/api-operation-web/banner/org/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/公司广告管理/广告位查询")
def banner_org_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/公司广告管理/广告位查询"
    url = f"/api-operation-web/banner/org/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/公司广告管理/广告位更新")
def banner_org_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/公司广告管理/广告位更新"
    url = f"/api-operation-web/banner/org/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/公司广告管理/广告位删除")
def banner_org_delete_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/公司广告管理/广告位删除"
    url = f"/api-operation-web/banner/org/delete"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/公司广告管理/广告位状态修改")
def banner_org_changeStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/公司广告管理/广告位状态修改"
    url = f"/api-operation-web/banner/org/changeStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/广告位新增")
def banner_popup_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/广告位新增"
    url = f"/api-operation-web/banner/popup/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/广告位查询")
def banner_popup_query_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/广告位查询"
    url = f"/api-operation-web/banner/popup/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/广告位更新")
def banner_popup_update_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/广告位更新"
    url = f"/api-operation-web/banner/popup/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/广告位删除")
def banner_popup_delete_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/广告位删除"
    url = f"/api-operation-web/banner/popup/delete"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/广告作废")
def banner_popup_expirePopups_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/广告作废"
    url = f"/api-operation-web/banner/popup/expirePopups"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销/营销广告/广告管理/弹窗广告管理/发送")
def banner_popup_sendPopup_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销/营销广告/广告管理/弹窗广告管理/发送"
    url = f"/api-operation-web/banner/popup/sendPopup"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

