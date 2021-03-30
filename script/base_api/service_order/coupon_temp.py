
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/优惠设置/优惠券/查看单个学生优惠券操作记录")
def coupon_queryOperationRecordByCouponItemId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryOperationRecordByCouponItemId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/上传学生名单")
def coupon_addCouponItemByUpload_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/addCouponItemByUpload"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/设置自动发行优惠券")
def coupon_updateAutoIssueConditionByCouponId_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/updateAutoIssueConditionByCouponId"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属课程")
def coupon_queryCoursesByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryCoursesByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改备注")
def coupon_updateRemark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/updateRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/删除优惠券")
def coupon_delete_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/delete"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询自动发行优惠券")
def coupon_queryAutoIssueConditionByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryAutoIssueConditionByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/新增优惠券")
def coupon_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属校区")
def coupon_querySchoolsByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/querySchoolsByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改优惠券状态")
def coupon_updateStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查看单个优惠券操作记录")
def coupon_queryOperationRecordByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryOperationRecordByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询单个优惠券")
def coupon_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/前台业务/学生信息/发放新生优惠券")
def coupon_distributeAutoCouponByNewStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/coupon/distributeAutoCouponByNewStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("系统设置/优惠设置/优惠券/查询优惠券列表")
def coupon_queryAll_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查看优惠券使用情况")
def coupon_queryUse_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryUse"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/导出上传的学生名单")
def coupon_exportUploadData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/exportUploadData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/pc端获取可使用优惠券")
def coupon_queryMatchCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryMatchCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属班级")
def coupon_queryClassesByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/queryClassesByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改学生优惠券状态")
def coupon_updateCouponItemStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/updateCouponItemStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/在线添加学生")
def coupon_addCouponItemByOnline_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/addCouponItemByOnline"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/删除学生优惠券")
def coupon_deleteCouponItem_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/deleteCouponItem"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/筛选花名册添加")
def coupon_addCouponItemBySelectStudent_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/addCouponItemBySelectStudent"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/继续提交学生名单")
def coupon_addCouponItemByKey_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/addCouponItemByKey"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/编辑优惠券")
def coupon_edit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/coupon/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券张数")
def coupon_countMyValidCouponItem_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/coupon/countMyValidCouponItem"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券列表")
def coupon_queryMyCouponItemList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/coupon/queryMyCouponItemList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券详情")
def coupon_queryCouponItemDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/coupon/queryCouponItemDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/根据优惠券查询学生可报名班级")
def coupon_queryClassesByCoupon_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/coupon/queryClassesByCoupon"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询单个优惠券")
def coupon_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/新增优惠券")
def coupon_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/编辑优惠券")
def coupon_edit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/edit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠/更改优惠状态")
def coupon_updateStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/删除优惠券")
def coupon_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改备注")
def coupon_updateRemark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/updateRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查看优惠券使用情况")
def coupon_queryUse_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryUse"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/修改学生优惠券状态")
def coupon_updateCouponItemStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/updateCouponItemStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/删除学生优惠券")
def coupon_couponItem_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/couponItem"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/设置自动发行优惠券")
def coupon_updateAutoIssueCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/updateAutoIssueCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询自动发行优惠券")
def coupon_queryAutoIssueConditionByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryAutoIssueConditionByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("系统设置/优惠设置/优惠券/查询优惠券列表")
def coupon_queryAll_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/上传学生名单")
def coupon_addCouponItemByUpload_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/addCouponItemByUpload"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/继续提交学生名单")
def coupon_addCouponItemByKey_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/addCouponItemByKey"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/在线添加学生")
def coupon_addCouponItemByOnline_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/addCouponItemByOnline"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/筛选花名册添加")
def coupon_addCouponItemBySelectStudent_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/addCouponItemBySelectStudent"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属课程")
def coupon_queryCoursesByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryCoursesByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属班级")
def coupon_queryClassesByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryClassesByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查询优惠券所属校区")
def coupon_querySchoolsByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/querySchoolsByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/新增优惠券")
def coupon_queryOperationRecordByCouponId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryOperationRecordByCouponId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/查看单个优惠券操作记录")
def coupon_queryOperationRecordByCouponItemId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/queryOperationRecordByCouponItemId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/优惠设置/优惠券/导出上传的学生名单")
def coupon_exportUploadData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/coupon/exportUploadData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券数量")
def coupon_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/coupon/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券列表")
def coupon_list_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/coupon/list"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/我的主页/优惠券详情")
def coupon_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_mini/coupon/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

