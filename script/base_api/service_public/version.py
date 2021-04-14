
from common.run_method import RunMethod
import allure


@allure.step("通用/App资源/获取热更新资源two")
def version_platform_platform_available_get(platform, params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "通用/App资源/获取热更新资源two"
    url = f"/service-public/version/{platform}/platform/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

