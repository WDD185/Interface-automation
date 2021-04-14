
from common.run_method import RunMethod
import allure


@allure.step("小程序/基础/发送短信验证码")
def verificationCode_receiveVerificationCode_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "小程序/基础/发送短信验证码"
    url = f"/service-user/verificationCode/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/首页/用户发送验证码")
def verificationCode_receiveVerificationCode_customer_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/首页/用户发送验证码"
    url = f"/service-user/verificationCode/receiveVerificationCode/customer"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

