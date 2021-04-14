
from common.run_method import RunMethod
import allure


@allure.step("极运营/入学诊断/诊断列表查询")
def diagnosis_queryDiagnosticDetailList_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/入学诊断/诊断列表查询"
    url = f"/service-gos/diagnosis/queryDiagnosticDetailList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/入学诊断/查询诊断名单学生信息")
def diagnosis_queryDiagnosticStudentsPageList_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/入学诊断/查询诊断名单学生信息"
    url = f"/service-gos/diagnosis/queryDiagnosticStudentsPageList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/入学诊断/获取试卷")
def diagnosis_exam_paper_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/入学诊断/获取试卷"
    url = f"/service-gos/diagnosis/exam/paper"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/入学诊断/查询诊断报告详情")
def diagnosis_report_detail_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/入学诊断/查询诊断报告详情"
    url = f"/service-gos/diagnosis/report/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

