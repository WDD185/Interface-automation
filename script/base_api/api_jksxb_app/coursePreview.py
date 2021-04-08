
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮app/班级详情/查询课程大纲")
def coursePreview_getCourseOutLine_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-jksxb-app/coursePreview/getCourseOutLine"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮app/班级详情/查询预热知识包详情")
def coursePreview_getPackageData_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/api-jksxb-app/coursePreview/getPackageData"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

