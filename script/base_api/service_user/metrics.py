
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("通用/app数据上报")
def metrics_appMetrics_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "通用/app数据上报"
    url = f"/service-user/metrics/appMetrics"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

