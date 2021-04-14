
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮app/班级详情/查询课程大纲")
def coursePreview_getCourseOutLine_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮app/班级详情/查询课程大纲"
    url = f"/api-jksxb-app/coursePreview/getCourseOutLine"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮app/班级详情/查询预热知识包详情")
def coursePreview_getPackageData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮app/班级详情/查询预热知识包详情"
    url = f"/api-jksxb-app/coursePreview/getPackageData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

