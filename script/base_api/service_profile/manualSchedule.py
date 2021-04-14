
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/极客资料/手动发送开课前极客资料")
def manualSchedule_sendBeforeClassGeekMaterial_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/极客资料/手动发送开课前极客资料"
    url = f"/service-profile/manualSchedule/sendBeforeClassGeekMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/预习数据/手动处理预习数据")
def manualSchedule_addPreviewData_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/预习数据/手动处理预习数据"
    url = f"/service-profile/manualSchedule/addPreviewData"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

