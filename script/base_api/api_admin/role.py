
from common.run_method import RunMethod
import allure


@allure.step("极权限/根据员工ID查询为角色组管理员的所有角色分组")
def role_queryMasterRoleTreeByEmployeeId_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/根据员工ID查询为角色组管理员的所有角色分组"
    url = f"/api-admin/role/queryMasterRoleTreeByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极权限/根据员工ID查询角色树")
def role_queryRoleTreeByEmployeeId_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/根据员工ID查询角色树"
    url = f"/api-admin/role/queryRoleTreeByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极权限/添加角色")
def role_addRole_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/添加角色"
    url = f"/api-admin/role/addRole"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极权限/添加角色组")
def role_addRoleGroup_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/添加角色组"
    url = f"/api-admin/role/addRoleGroup"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极权限/删除角色组")
def role_deleteRoleGroup_delete(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/删除角色组"    
    url = f"/api-admin/role/deleteRoleGroup"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极权限/删除角色")
def role_deleteRole_delete(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/删除角色"    
    url = f"/api-admin/role/deleteRole"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极权限/查询员工对应的所有角色")
def role_queryRolesByEmployeeId_get(params=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/查询员工对应的所有角色"
    url = f"/api-admin/role/queryRolesByEmployeeId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极权限/修改员工与角色绑定关系")
def role_updateEmployeeRoles_put(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/修改员工与角色绑定关系"    
    url = f"/api-admin/role/updateEmployeeRoles"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)  
    return res


@allure.step("极权限/修改角色组名称")
def role_updateRoleGroupName_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/修改角色组名称"
    url = f"/api-admin/role/updateRoleGroupName"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极权限/修改角色名称")
def role_updateRoleName_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/修改角色名称"
    url = f"/api-admin/role/updateRoleName"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极权限/根据角色ID查询员工列表")
def role_queryEmployeesByRoleId_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/根据角色ID查询员工列表"
    url = f"/api-admin/role/queryEmployeesByRoleId"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极权限/删除员工角色关系")
def role_deleteEmployeeRole_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/删除员工角色关系"
    url = f"/api-admin/role/deleteEmployeeRole"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res


@allure.step("极权限/角色添加员工信息")
def role_addEmployeeByRoleId_post(params=None, body=None, header=None, return_json=True, **kwargs):
    '''
    :param: url地址后面的参数
    :body: 请求体
    :return_json: 是否返回json格式的响应（默认是）
    :header: 请求的header
    :host: 请求的环境
    :return: 默认json格式的响应， return_json=False返回原始响应
    '''
    name = "极权限/角色添加员工信息"
    url = f"/api-admin/role/addEmployeeByRoleId"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs) 
    return res

