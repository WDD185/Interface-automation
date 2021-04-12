
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("JkyApp/查询班级花名册")
def memberships_classes_students_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyApp/查询班级花名册"
    url = f"/api-operation-app/memberships/classes/students"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

