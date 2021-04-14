
from common.run_method import RunMethod
import allure


@allure.step("备课评价/新增评价")
def courseWareEvaluateController_addEvaluate_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "备课评价/新增评价"
    url = f"/service-research/courseWareEvaluateController/addEvaluate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("备课评价/根据课件查询评价")
def courseWareEvaluateController_queryEvaluateList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "备课评价/根据课件查询评价"
    url = f"/service-research/courseWareEvaluateController/queryEvaluateList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("备课评价/评价列表")
def courseWareEvaluateController_queryEvaluateByParam_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "备课评价/评价列表"
    url = f"/service-research/courseWareEvaluateController/queryEvaluateByParam"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("备课评价/查询评价详情")
def courseWareEvaluateController_queryEvaluateById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "备课评价/查询评价详情"
    url = f"/service-research/courseWareEvaluateController/queryEvaluateById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("备课评价/删除评价")
def courseWareEvaluateController_deleteEvaluate_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "备课评价/删除评价"
    url = f"/service-research/courseWareEvaluateController/deleteEvaluate"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("备课评价/查询评价列表")
def courseWareEvaluateController_queryEvaluateListById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "备课评价/查询评价列表"
    url = f"/service-research/courseWareEvaluateController/queryEvaluateListById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

