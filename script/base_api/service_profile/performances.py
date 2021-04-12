
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况")
def performances_details_studentId_student_classes_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况"
    url = f"/service-profile/performances/details/{studentId}/student/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

