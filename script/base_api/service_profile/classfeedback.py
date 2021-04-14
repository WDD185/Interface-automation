
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取未读班贴数量")
def classfeedback_student_unread_note_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户行课班帖/获取未读班贴数量"
    url = f"/service-profile/classfeedback/student/unread/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴列表")
def classfeedback_student_notes_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生班贴列表"
    url = f"/service-profile/classfeedback/student/notes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴详情")
def classfeedback_student_note_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生班贴详情"
    url = f"/service-profile/classfeedback/student/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生具体某堂课的班帖详情")
def classfeedback_classId_class_studentId_student_get(classId, studentId, params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生具体某堂课的班帖详情"
    url = f"/service-profile/classfeedback/{classId}/class/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

