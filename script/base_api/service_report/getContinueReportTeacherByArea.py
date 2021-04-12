
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/统计报表/钉钉查看续班率BY区域大区老师")
def getContinueReportTeacherByArea_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/统计报表/钉钉查看续班率BY区域大区老师"
    url = f"/service-report/getContinueReportTeacherByArea"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

