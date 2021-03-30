
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("小程序/营销中心/cms管理/获取单个数据")
def carousel_cms_getBannerCms_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/carousel/cms/getBannerCms"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/cms管理/获取列表数据")
def carousel_cms_getBannerCmsList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/carousel/cms/getBannerCmsList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/cms管理/增加数据")
def carousel_cms_addBannerCms_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/carousel/cms/addBannerCms"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/cms管理/更新数据")
def carousel_cms_bannerCms_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/carousel/cms/bannerCms"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/cms管理/删除数据")
def carousel_cms_bannerCms_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_gos/carousel/cms/bannerCms"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

