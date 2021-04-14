
from common.run_method import RunMethod
import allure


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况")
def performances_details_studentId_student_classes_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况"
    url = f"/service-profile/performances/details/{studentId}/student/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res

