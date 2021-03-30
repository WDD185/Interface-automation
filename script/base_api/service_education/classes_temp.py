
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/优惠设置/新增优惠(旧)")
def classes_discounts_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/删除优惠(旧)")
def classes_discounts_delete_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/delete"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/查询优惠(旧)")
def classes_discounts_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/修改优惠(旧)")
def classes_discounts_update_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/update"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/订单班级验证")
def classes_discounts_discount_valideClass_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/discount/valideClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/优惠匹配")
def classes_discounts_discount_calculate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/discount/calculate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/查询材料费")
def classes_discounts_material_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/classes/discounts/material"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班级推送/查看班级推送情况")
def classes_classId_purchases_anotherClassId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/{classId}/purchases/{anotherClassId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取授课老师信息")
def classes_teacher_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/teacher"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生未读班贴的数量")
def classes_unattended_student_studentId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/unattended/student/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/花名册/获取调出课次")
def classes_classId_schedules_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/{classId}/schedules"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/班级/查询班级座次")
def classes_classId_seats_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/{classId}/seats"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/课表/修改班级座次")
def classes_classId_seats_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/{classId}/seats"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的详细列表")
def classes_studentId_student_unfinished_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/{studentId}/student/unfinished"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的班级行课进度情况")
def classes_progress_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/progress/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班级推送/查询班级")
def classes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班级推送/查询可推送班级")
def classes_canPush_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/canPush"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生已经报的班级")
def classes_reading_student_studentId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/reading/student/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班级推送/向学生推送班级")
def classes_classId_purchases_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/classes/{classId}/purchases"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询班级列表")
def classes_queryList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/classes/queryList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询班级座位列表")
def classes_seats_queryByClassId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/classes/seats/queryByClassId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyApp/查询订单班级列表")
def classes_order_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/classes/order/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP订单查询班级")
def classes_order_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/classes/order/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

