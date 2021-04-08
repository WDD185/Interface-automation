
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通/首页/教师任职信息")
def jst_home_teacher_msg_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/jst-home/teacher/msg"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页/在读班级和学生")
def jst_home_teachers_reading_msg_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + f"/service-education/jst-home/teachers/reading-msg"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

