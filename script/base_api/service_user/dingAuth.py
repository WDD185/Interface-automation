
from common.run_method import RunMethod
import allure


@allure.step("用户/钉钉/h5免密登录")
def dingAuth_h5_periodicalAuth_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "用户/钉钉/h5免密登录"
    url = f"/service-user/dingAuth/h5/periodicalAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("教师基本功大赛/钉钉登录")
def dingAuth_h5_basicSkillAuth_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "教师基本功大赛/钉钉登录"
    url = f"/service-user/dingAuth/h5/basicSkillAuth"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

