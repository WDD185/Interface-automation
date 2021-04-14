
from common.run_method import RunMethod
import allure


@allure.step("极运营/班主任机制/沟通记录/新增沟通记录")
def communicate_record_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/沟通记录/新增沟通记录"
    url = f"/service-crm/communicate/record"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/班主任机制/沟通记录/修改沟通记录")
def communicate_record_put(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/沟通记录/修改沟通记录"    
    url = f"/service-crm/communicate/record"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/班主任机制/沟通记录/根据学生ID查找记录列表")
def communicate_record_records_studentId_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/沟通记录/根据学生ID查找记录列表"
    url = f"/service-crm/communicate/record/records/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/班主任机制/沟通记录/查询所有沟通类型数组")
def communicate_record_types_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/沟通记录/查询所有沟通类型数组"
    url = f"/service-crm/communicate/record/types"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/班主任机制/沟通记录/根据记录ID和类型查找记录详情")
def communicate_record_record_recordId_get(recordId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/班主任机制/沟通记录/根据记录ID和类型查找记录详情"
    url = f"/service-crm/communicate/record/record/{recordId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("CRM/班级学员沟通记录列表")
def communicate_record_getRecordByClass_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "CRM/班级学员沟通记录列表"
    url = f"/service-crm/communicate/record/getRecordByClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/CRM/学员管理/我的班级/班级学员沟通记录/导出")
def communicate_record_exportRecordByClass_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/CRM/学员管理/我的班级/班级学员沟通记录/导出"
    url = f"/service-crm/communicate/record/exportRecordByClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("按类型获取沟通记录")
def communicate_record_getStudentRecordByType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "按类型获取沟通记录"
    url = f"/service-crm/communicate/record/getStudentRecordByType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极运营/CRM/学员管理/我的班级/班级学员沟通记录/批量导入沟通记录/下载模板")
def communicate_record_downModel_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/CRM/学员管理/我的班级/班级学员沟通记录/批量导入沟通记录/下载模板"
    url = f"/service-crm/communicate/record/downModel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极运营/CRM/学员管理/我的班级/班级学员沟通记录/批量导入沟通记录/上传excel")
def communicate_record_batchCreateCommunicateRecords_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极运营/CRM/学员管理/我的班级/班级学员沟通记录/批量导入沟通记录/上传excel"
    url = f"/service-crm/communicate/record/batchCreateCommunicateRecords"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极师通/花名册/新增沟通记录")
def communicate_record_insertJst_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/花名册/新增沟通记录"
    url = f"/service-crm/communicate/record/insertJst"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极师通/花名册/查询单个学生沟通记录")
def communicate_record_getByStudentIdAndClassIdJst_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/花名册/查询单个学生沟通记录"
    url = f"/service-crm/communicate/record/getByStudentIdAndClassIdJst"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极师通/花名册/编辑沟通记录")
def communicate_record_updateJst_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极师通/花名册/编辑沟通记录"
    url = f"/service-crm/communicate/record/updateJst"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

