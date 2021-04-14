
from common.run_method import RunMethod
import allure


@allure.step("极运营/营销中心/业绩归属/修改介绍人")
def web_performance_change_employee_id_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/业绩归属/修改介绍人"
    url = f"/service-finance/web/performance/change/employee/id"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/业绩归属/修改业绩归属人")
def web_performance_change_introducerStudent_id_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/业绩归属/修改业绩归属人"
    url = f"/service-finance/web/performance/change/introducerStudent/id"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/业绩归属/业绩归属明细")
def web_performance_queryOrderDetailList_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/业绩归属/业绩归属明细"
    url = f"/service-finance/web/performance/queryOrderDetailList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/营销中心/业绩归属/无业绩归属人明细")
def web_performance_queryPerformanceDetailList_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/营销中心/业绩归属/无业绩归属人明细"
    url = f"/service-finance/web/performance/queryPerformanceDetailList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

