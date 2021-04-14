
from common.run_method import RunMethod
import allure


@allure.step("极师通/备课/备课教材查询")
def prepareLessons_prepareTextbook_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/备课/备课教材查询"
    url = f"/service-research/prepareLessons/prepareTextbook"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极师通/备课/备课教材可关联班级")
def prepareLessons_textbook_classes_available_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/备课/备课教材可关联班级"
    url = f"/service-research/prepareLessons/textbook/classes/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极师通/备课/新增备课教材")
def prepareLessons_prepareTextbook_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/备课/新增备课教材"
    url = f"/service-research/prepareLessons/prepareTextbook"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极师通/备课/删除备课教材")
def prepareLessons_prepareTextbook_delete(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/备课/删除备课教材"    
    url = f"/service-research/prepareLessons/prepareTextbook"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极师通/备课/教材/查询班级是否关联了教材")
def prepareLessons_related_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/备课/教材/查询班级是否关联了教材"
    url = f"/service-research/prepareLessons/related"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极师通/备课/教师可用教材查询")
def prepareLessons_textbook_available_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/备课/教师可用教材查询"
    url = f"/service-research/prepareLessons/textbook/available"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

