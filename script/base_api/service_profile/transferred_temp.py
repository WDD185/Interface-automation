
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/用户行课/获取某个课程总的调课次数")
def transferred_classId_class_totalNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/transferred/{classId}/class/totalNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个课程的某一讲能够调入的班级和讲次")
def transferred_classId_class_classScheduleId_section_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/transferred/{classId}/class/{classScheduleId}/section"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

