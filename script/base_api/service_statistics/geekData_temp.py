
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极数据/权限部门查询")
def geekData_areaRelation_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/areaRelation"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/全部目标方案")
def geekData_allTarget_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/allTarget"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/人次/折线图")
def geekData_personTimeRange_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/personTimeRange"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/人次/明细")
def geekData_personTimeDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/personTimeDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/人次/汇总")
def geekData_personTimeCount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/personTimeCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/人次/完成率")
def geekData_personTimeAchieveRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/personTimeAchieveRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/续报率/数据查询")
def geekData_continueRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/continueRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/续报率/折线图")
def geekData_continueRateRange_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/continueRateRange"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/满班率")
def geekData_fullClassRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/fullClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/退费率/总经办&区域校长")
def geekData_refund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/退费率/中心校主管")
def geekData_refundForCenterMaster_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/refundForCenterMaster"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/续报率/年级数据")
def geekData_continueRate_grade_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/continueRate/grade"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/续报率/明细")
def geekData_continueRate_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/continueRate/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/满班率/明细")
def geekData_fullClassRate_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/fullClassRate/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/退费率/明细")
def geekData_refund_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/refund/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/层级校区")
def geekData_treeSchools_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/treeSchools"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/首页/PK")
def geekData_index_static_pk_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/index/static/pk"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/首页/目标完成榜")
def geekData_index_achieve_rank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/index/achieve/rank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/首页/入口年级")
def geekData_index_entry_continue_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_statistics/geekData/index/entry/continue"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

