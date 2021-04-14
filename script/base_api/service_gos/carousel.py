
from common.run_method import RunMethod
import allure


@allure.step("小程序/营销中心/cms管理/获取单个数据")
def carousel_cms_getBannerCms_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "小程序/营销中心/cms管理/获取单个数据"
    url = f"/service-gos/carousel/cms/getBannerCms"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/营销中心/cms管理/获取列表数据")
def carousel_cms_getBannerCmsList_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/cms管理/获取列表数据"
    url = f"/service-gos/carousel/cms/getBannerCmsList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/cms管理/增加数据")
def carousel_cms_addBannerCms_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/cms管理/增加数据"
    url = f"/service-gos/carousel/cms/addBannerCms"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/cms管理/更新数据")
def carousel_cms_bannerCms_put(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/cms管理/更新数据"    
    url = f"/service-gos/carousel/cms/bannerCms"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/营销中心/cms管理/删除数据")
def carousel_cms_bannerCms_delete(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/cms管理/删除数据"    
    url = f"/service-gos/carousel/cms/bannerCms"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res

