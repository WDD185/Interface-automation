
from common.run_method import RunMethod
import allure


@allure.step("管理内刊/查阅端/干部内刊列表")
def periodical_listPeriodicals_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "管理内刊/查阅端/干部内刊列表"
    url = f"/api-periodical/periodical/listPeriodicals"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("管理内刊/查阅端/干部内刊内容")
def periodical_listPeriodicalContents_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "管理内刊/查阅端/干部内刊内容"
    url = f"/api-periodical/periodical/listPeriodicalContents"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("管理内刊/查阅端/干部内刊内容免鉴权查看")
def periodical_listPeriodicalContentsNoAuth_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "管理内刊/查阅端/干部内刊内容免鉴权查看"
    url = f"/api-periodical/periodical/listPeriodicalContentsNoAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("管理内刊/查阅端/干部内刊书架")
def periodical_listPeriodicalsOnReadNum_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "管理内刊/查阅端/干部内刊书架"
    url = f"/api-periodical/periodical/listPeriodicalsOnReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

