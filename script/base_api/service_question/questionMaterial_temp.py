
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极题库")
def questionMaterial_uploadImages_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/uploadImages"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def questionMaterial_updateLibraryStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/updateLibraryStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def questionMaterial_putToLibrary_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/putToLibrary"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通")
def questionMaterial_uploadMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/uploadMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通")
def questionMaterial_deleteMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/deleteMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通")
def questionMaterial_getMaterialsByGstPage_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/getMaterialsByGstPage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通")
def questionMaterial_updateMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/updateMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库")
def questionMaterial_getMaterialsByGtkPage_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/getMaterialsByGtkPage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/添加老师区域归属")
def questionMaterial_addOrModTeacherMaterialDepartment_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/addOrModTeacherMaterialDepartment"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/查询老师区域归属")
def questionMaterial_getTeacherMaterialDepartment_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/getTeacherMaterialDepartment"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极题库/上传人历史地址")
def questionMaterial_getHistoryAddress_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_question/questionMaterial/getHistoryAddress"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

