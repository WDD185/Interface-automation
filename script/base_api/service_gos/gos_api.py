
from common.run_method import RunMethod


def gos_api_package_check_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "小程序/商品/套餐检查服务"
    url = f"/service-gos/gos-api/package/check"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


def gos_api_goods_check_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "小程序/商品/商品检查服务"
    url = f"/service-gos/gos-api/goods/check"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

