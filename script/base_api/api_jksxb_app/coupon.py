
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/我的/优惠券张数")
def coupon_countMyValidCouponItem_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/我的/优惠券张数"
    url = f"/api-jksxb-app/coupon/countMyValidCouponItem"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券列表")
def coupon_queryMyCouponItemList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/我的/优惠券列表"
    url = f"/api-jksxb-app/coupon/queryMyCouponItemList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券详情")
def coupon_queryCouponItemDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/我的/优惠券详情"
    url = f"/api-jksxb-app/coupon/queryCouponItemDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/根据优惠券查询学生可报名班级")
def coupon_queryClassesByCoupon_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/根据优惠券查询学生可报名班级"
    url = f"/api-jksxb-app/coupon/queryClassesByCoupon"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

