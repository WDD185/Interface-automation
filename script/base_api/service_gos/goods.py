
from common.run_method import RunMethod
import allure


@allure.step("极运营/营销中心/商品中心/新建编辑商品")
def goods_course_saveGoods_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/商品中心/新建编辑商品"
    url = f"/service-gos/goods/course/saveGoods"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/商品中心/面授课程商品列表")
def goods_course_goodsList_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/商品中心/面授课程商品列表"
    url = f"/service-gos/goods/course/goodsList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/商品中心/商品详情")
def goods_course_goodsDetail_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/商品中心/商品详情"
    url = f"/service-gos/goods/course/goodsDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/营销中心/商品中心/停用启用商品")
def goods_course_updateGoodsStatus_patch(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/商品中心/停用启用商品"
    url = f"/service-gos/goods/course/updateGoodsStatus"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/营销中心/商品中心/删除商品")
def goods_course_deleteGoods_delete(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/商品中心/删除商品"    
    url = f"/service-gos/goods/course/deleteGoods"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res

