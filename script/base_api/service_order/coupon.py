
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/优惠设置/优惠券/查看单个学生优惠券操作记录")
def coupon_queryOperationRecordByCouponItemId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryOperationRecordByCouponItemId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/上传学生名单")
def coupon_addCouponItemByUpload_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/addCouponItemByUpload"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/设置自动发行优惠券")
def coupon_updateAutoIssueConditionByCouponId_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/updateAutoIssueConditionByCouponId"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属课程")
def coupon_queryCoursesByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryCoursesByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改备注")
def coupon_updateRemark_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/updateRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/删除优惠券")
def coupon_delete_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/delete"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询自动发行优惠券")
def coupon_queryAutoIssueConditionByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryAutoIssueConditionByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/新增优惠券")
def coupon_add_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属校区")
def coupon_querySchoolsByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/querySchoolsByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改优惠券状态")
def coupon_updateStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查看单个优惠券操作记录")
def coupon_queryOperationRecordByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryOperationRecordByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询单个优惠券")
def coupon_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("系统设置/优惠设置/优惠券/查询优惠券列表")
def coupon_queryAll_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查看优惠券使用情况")
def coupon_queryUse_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryUse"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/导出上传的学生名单")
def coupon_exportUploadData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/exportUploadData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/pc端获取可使用优惠券")
def coupon_queryMatchCoupon_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryMatchCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属班级")
def coupon_queryClassesByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/queryClassesByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改学生优惠券状态")
def coupon_updateCouponItemStatus_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/updateCouponItemStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/在线添加学生")
def coupon_addCouponItemByOnline_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/addCouponItemByOnline"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/删除学生优惠券")
def coupon_deleteCouponItem_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/deleteCouponItem"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/筛选花名册添加")
def coupon_addCouponItemBySelectStudent_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/addCouponItemBySelectStudent"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/继续提交学生名单")
def coupon_addCouponItemByKey_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/addCouponItemByKey"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/编辑优惠券")
def coupon_edit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-order/coupon/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

