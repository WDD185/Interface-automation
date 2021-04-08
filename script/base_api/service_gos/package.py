
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/营销中心/商品中心/新建编辑套餐")
def package_course_savePackage_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/package/course/savePackage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/商品中心/套餐商品列表")
def package_course_packageList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/package/course/packageList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/商品中心/套餐详情")
def package_course_packageDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/package/course/packageDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/商品中心/停用启用套餐")
def package_course_updatePackageStatus_patch(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/package/course/updatePackageStatus"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/商品中心/删除套餐")
def package_course_deletePackage_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-gos/package/course/deletePackage"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

