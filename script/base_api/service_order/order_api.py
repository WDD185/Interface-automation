
from common.run_method import RunMethod
import allure


@allure.step("小程序/订单/根据订单状态查询订单数量")
def order_api_inner_order_order_countByStatuses_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "小程序/订单/根据订单状态查询订单数量"
    url = f"/service-order/order-api/inner-order/order/countByStatuses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/系统设置/优惠券/优惠券查询服务")
def order_api_inner_order_queryCoupon_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/系统设置/优惠券/优惠券查询服务"
    url = f"/service-order/order-api/inner-order/queryCoupon"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

