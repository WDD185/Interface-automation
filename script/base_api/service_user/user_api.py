
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极运营/系统设置/校区设置/校区详情服务")
def user_api_user_department_school_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/校区设置/校区详情服务"
    url = f"/service-user/user-api/user/department/school/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/校区设置/校区查询服务")
def user_api_user_department_school_querySchoolByCondition_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/校区设置/校区查询服务"
    url = f"/service-user/user-api/user/department/school/querySchoolByCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/关于极客/栏目列表服务")
def user_api_user_company_columns_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/系统设置/关于极客/栏目列表服务"
    url = f"/service-user/user-api/user/company/columns"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

