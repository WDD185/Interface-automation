
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("线上商店-团购&订单/团购列表")
def group_order_listGroupPurchases_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-团购&订单/团购列表"
    url = f"/service-gos/group/order/listGroupPurchases"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-团购&订单/拼团订单列表")
def group_order_listMyGroupOrders_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-团购&订单/拼团订单列表"
    url = f"/service-gos/group/order/listMyGroupOrders"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-团购&订单/团详详情")
def group_order_getGroupPurchaseDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-团购&订单/团详详情"
    url = f"/service-gos/group/order/getGroupPurchaseDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-小程序分享/获取小程序分享详情")
def group_qr_getShareDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-小程序分享/获取小程序分享详情"
    url = f"/service-gos/group/qr/getShareDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-小程序分享/获取活动班级二维码")
def group_qr_classQr_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-小程序分享/获取活动班级二维码"
    url = f"/service-gos/group/qr/classQr"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("线上商店-小程序分享/获取组团二维码")
def group_qr_groupQr_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "线上商店-小程序分享/获取组团二维码"
    url = f"/service-gos/group/qr/groupQr"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/组团详情")
def group_center_groupDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/组团详情"
    url = f"/service-gos/group/center/groupDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购订单/团购订单列表")
def group_order_orderList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购订单/团购订单列表"
    url = f"/service-gos/group/order/orderList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/组团列表")
def group_center_groupList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/组团列表"
    url = f"/service-gos/group/center/groupList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/活动详情")
def group_center_activityDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/活动详情"
    url = f"/service-gos/group/center/activityDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/删除活动")
def group_center_deleteActivity_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/删除活动"    
    url = f"/service-gos/group/center/deleteActivity"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/停用启用活动")
def group_center_updateActivityStatus_patch(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/停用启用活动"
    url = f"/service-gos/group/center/updateActivityStatus"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/活动列表")
def group_center_activityList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/活动列表"
    url = f"/service-gos/group/center/activityList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/新增编辑活动")
def group_center_saveActivity_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/新增编辑活动"
    url = f"/service-gos/group/center/saveActivity"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购订单/退款")
def group_operate_refund_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购订单/退款"
    url = f"/service-gos/group/operate/refund"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购订单/团购订单总费用")
def group_order_getTotalAmount_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购订单/团购订单总费用"
    url = f"/service-gos/group/order/getTotalAmount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购订单/详情")
def group_operate_refundDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购订单/详情"
    url = f"/service-gos/group/operate/refundDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/订单状态查询")
def group_order_getOrderStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/订单/订单状态查询"
    url = f"/service-gos/group/order/getOrderStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/预支付")
def group_operate_prePay_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/订单/预支付"
    url = f"/service-gos/group/operate/prePay"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/在线商城/支付前验证")
def group_micoApp_queryStudentActiveOrder_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/在线商城/支付前验证"
    url = f"/service-gos/group/micoApp/queryStudentActiveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/拼团中、拼团成功、拼团失败、分享打开")
def group_micoApp_groupOrderDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/拼团中、拼团成功、拼团失败、分享打开"
    url = f"/service-gos/group/micoApp/groupOrderDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页详情")
def group_micoApp_activeClassDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/首页详情"
    url = f"/service-gos/group/micoApp/activeClassDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/首页")
def group_micoApp_index_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/首页"
    url = f"/service-gos/group/micoApp/index"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/取消订单")
def group_order_cancelGroupOrder_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/订单/取消订单"
    url = f"/service-gos/group/order/cancelGroupOrder"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/订单/团购下单")
def group_order_order_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/订单/团购下单"
    url = f"/service-gos/group/order/order"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/商品详情/参团信息")
def group_micoApp_getActiveJoinGroup_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/商品详情/参团信息"
    url = f"/service-gos/group/micoApp/getActiveJoinGroup"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/小程序码生成")
def group_qr_getQr_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/小程序码生成"
    url = f"/service-gos/group/qr/getQr"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购中心/分享活动二维码")
def group_qr_share_miniProgram_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购中心/分享活动二维码"
    url = f"/service-gos/group/qr/share/miniProgram"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购订单/导出订单")
def group_order_orderList_export_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购订单/导出订单"
    url = f"/service-gos/group/order/orderList/export"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/营销中心/团购订单/一键成团")
def group_order_forceMergeGroup_activityId_post(activityId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/营销中心/团购订单/一键成团"
    url = f"/service-gos/group/order/forceMergeGroup/{activityId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("小程序/商品/活动校区列表")
def group_micoApp_activity_schoolAreas_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "小程序/商品/活动校区列表"
    url = f"/service-gos/group/micoApp/activity/schoolAreas"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

