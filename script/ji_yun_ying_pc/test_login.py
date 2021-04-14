from script.ji_yun_ying_pc.data_config import data_config
import jsonpath
from script.base_api.service_user.auth import auth_employee_post
from script.base_api.service_user.employees import *
from script.base_api.service_user.token import token_valid_get
import allure
import pytest


@allure.feature("不同账号的登录测试")
@allure.testcase("http://132.232.109.76/zentao/testcase-view-24250-1.html")
class TestLogin:

    header = {"Content-Type": "application/json;charset=UTF-8"}

    @allure.story("测试登录")
    @pytest.mark.parametrize("body_data", data_config.login_data)
    def test_login(self, body_data):
        # 登录
        res_json = auth_employee_post(body=body_data, header=TestLogin.header)
        tokens = jsonpath.jsonpath(res_json, "$.data.token")
        if tokens:
            token = tokens[0]
        else:
            token = "not found"
        TestLogin.header["Authorization"] = "Bearer " + token

        # 获取用户信息
        params = {"token": token}
        res_json = employees_info_get(params=params, header=TestLogin.header)
        employee_ids = jsonpath.jsonpath(res_json, "$..employeeId")
        employee_id = employee_ids[0] if employee_ids else "not found"
        # employee_names = jsonpath.jsonpath(res_json, "$..employeeName")
        # employee_name = employee_names[0] if employee_names else "not found"

        # 获取用户可用模块
        employees_employeeId_access_modules_get(employee_id, header=TestLogin.header)

        # 判断token是否有效
        token_valid_get(header=TestLogin.header)

