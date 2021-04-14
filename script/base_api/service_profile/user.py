
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码")
def user_studentId_backupMobilePhone_patch(studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码"
    url = f"/service-profile/user/{studentId}/backupMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码")
def user_studentId_bindingMobilePhone_patch(studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码"
    url = f"/service-profile/user/{studentId}/bindingMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录密码")
def user_type_signInPassword_patch(type, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/修改用户登录密码"
    url = f"/service-profile/user/{type}/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res

