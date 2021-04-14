
from common.run_method import RunMethod
import allure


@allure.step("极运营/人事管理/员工信息/批量导入/下载模板")
def batchEmp_downModel_emp_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/人事管理/员工信息/批量导入/下载模板"
    url = f"/service-user/batchEmp/downModel/emp"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/人事管理/员工信息/批量导入/上传文件导入")
def batchEmp_createEmp_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/人事管理/员工信息/批量导入/上传文件导入"
    url = f"/service-user/batchEmp/createEmp"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

