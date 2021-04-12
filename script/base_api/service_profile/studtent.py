
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户管理/修改当前学生用户的基础属性值")
def studtent_studentId_attribute_patch(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/修改当前学生用户的基础属性值"
    url = f"/service-profile/studtent/{studentId}/attribute"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

