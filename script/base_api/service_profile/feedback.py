
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题")
def feedback_mailbox_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题"
    url = f"/service-profile/feedback/mailbox"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户管理/向校长信箱反馈问题")
def feedback_mailbox_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/向校长信箱反馈问题"
    url = f"/service-profile/feedback/mailbox/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题上传的图片")
def feedback_feedbackId_mailbox_picture_get(feedbackId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题上传的图片"
    url = f"/service-profile/feedback/{feedbackId}/mailbox/picture"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

