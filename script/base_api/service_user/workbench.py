
from common.run_method import RunMethod
import allure


@allure.step("极运营/班主任机制/工作台/根据员工ID批量修改")
def workbench_menu_update_batch_employeeId_post(employeeId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/工作台/根据员工ID批量修改"
    url = f"/service-user/workbench/menu/update/batch/{employeeId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/班主任机制/工作台/根据员工ID查询")
def workbench_menu_employeeId_post(employeeId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/工作台/根据员工ID查询"
    url = f"/service-user/workbench/menu/{employeeId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

