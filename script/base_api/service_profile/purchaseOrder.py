
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中课程总数")
def purchaseOrder_studentId_student_count_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/获取某个学生购课单中课程总数"
    url = f"/service-profile/purchaseOrder/{studentId}/student/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/删除某个学生购课单中的某一条记录")
def purchaseOrder_purchaseId_studentstudentId_delete(purchaseId, studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/删除某个学生购课单中的某一条记录"    
    url = f"/service-profile/purchaseOrder/{purchaseId}/student{studentId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/某个学生向购课单中添加课程")
def purchaseOrder_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/某个学生向购课单中添加课程"
    url = f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量删除某个学生购课单中的多条记录")
def purchaseOrder_studentId_student_delete(studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/批量删除某个学生购课单中的多条记录"    
    url = f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中的课程")
def purchaseOrder_studentId_student_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/获取某个学生购课单中的课程"
    url = f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量修改某个学生购课单中多条记录的状态")
def purchaseOrder_studentId_student_put(studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/批量修改某个学生购课单中多条记录的状态"    
    url = f"/service-profile/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/修改某个学生购课单中某一条记录的状态")
def purchaseOrder_purchaseId_student_studentId_patch(purchaseId, studentId, params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户购课单/修改某个学生购课单中某一条记录的状态"
    url = f"/service-profile/purchaseOrder/{purchaseId}/student/{studentId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res

