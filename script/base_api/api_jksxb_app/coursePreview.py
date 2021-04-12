
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮app/班级详情/查询课程大纲")
def coursePreview_getCourseOutLine_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮app/班级详情/查询课程大纲"
    url = f"/api-jksxb-app/coursePreview/getCourseOutLine"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮app/班级详情/查询预热知识包详情")
def coursePreview_getPackageData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮app/班级详情/查询预热知识包详情"
    url = f"/api-jksxb-app/coursePreview/getPackageData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

