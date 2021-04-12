
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户行课/查询某班是否有效可报名")
def app_classes_studentId_queryIsEffectiveClasses_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/查询某班是否有效可报名"
    url = f"/service-education/app/classes/{studentId}/queryIsEffectiveClasses"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询某班是否设置教室以及所在校区是否支持选座")
def app_classes_isSupportChooseSeat_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/查询某班是否设置教室以及所在校区是否支持选座"
    url = f"/service-education/app/classes/isSupportChooseSeat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/就读学校名查询")
def app_setting_query_school_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/就读学校名查询"
    url = f"/service-education/app/setting/query/school"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/APP/查询可报班级/")
def app_classInfo_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/APP/查询可报班级/"
    url = f"/service-education/app/classInfo/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

