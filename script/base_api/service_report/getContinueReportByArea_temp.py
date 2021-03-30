
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/统计报表/钉钉查看续班率BY区域大区")
def getContinueReportByArea_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_report/getContinueReportByArea"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

