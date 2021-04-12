
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通App/教研/备课/查询老师及教材版本")
def jst_app_classes_getVersionNameByTeacherId_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/教研/备课/查询老师及教材版本"
    url = f"/service-education/jst-app/classes/getVersionNameByTeacherId"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

