
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/订单/计算订单总价")
def orderFlow_calculateOrderPrice_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/订单/计算订单总价"
    url = f"/api-jksxb-app/orderFlow/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/订单/预占座位")
def orderFlow_preTake_seat_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/订单/预占座位"
    url = f"/api-jksxb-app/orderFlow/preTake/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/订单/释放座位")
def orderFlow_cancle_seat_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/订单/释放座位"
    url = f"/api-jksxb-app/orderFlow/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/获取可使用优惠及优惠券")
def orderFlow_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/获取可使用优惠及优惠券"
    url = f"/api-jksxb-app/orderFlow/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/订单/下单前的预验证")
def orderFlow_preValidOrderCondition_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/订单/下单前的预验证"
    url = f"/api-jksxb-app/orderFlow/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/计算促销活动价格")
def orderFlow_calculatePromotion_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/计算促销活动价格"
    url = f"/api-jksxb-app/orderFlow/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/获取分段下可使用优惠及优惠券")
def orderFlow_queryDownMatchDiscountAndCoupon_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/获取分段下可使用优惠及优惠券"
    url = f"/api-jksxb-app/orderFlow/queryDownMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/订单/计算分段下订单总价")
def orderFlow_calculateDownOrderPrice_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/订单/计算分段下订单总价"
    url = f"/api-jksxb-app/orderFlow/calculateDownOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

