from common.run_method import RunMethod
from script.common_config import host
from script.ji_yun_ying_pc.common_config import public_assert
from script.ji_yun_ying_pc.data_config import data_config
import pytest
import allure
import jsonpath


@allure.step("登录接口")
def jyy_login(body_data):
    allure.dynamic.description(f"请求参数, body:{body_data}")
    url = host + "/service-user/auth/employee"
    res_json, res_header = RunMethod.run_main("POST", url, body_data=body_data, header=TestLogin.header)
    public_assert(res_json)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    allure.dynamic.description(f"请求参数, res_json:{res_json}")
    if tokens:
        return tokens[0]

@allure.step("获取员工信息接口")
def get_employee_info(token):
    url = host + f"/service-user/employees/info?token={token}"
    res_json, res_header = RunMethod.run_main("GET", url, header=TestLogin.header)
    public_assert(res_json)
    employee_id = jsonpath.jsonpath(res_json, "$..employeeId")
    employee_name = jsonpath.jsonpath(res_json, "$..employeeName")
    pytest.assume(employee_name is not None)
    pytest.assume(employee_name is not None)
    return employee_id[0], employee_name[0]


@allure.step("获取员工可用模块接口")
def get_employee_module(employee_id):
    url = host + f"/service-user/employees/{employee_id}/access/modules"
    res_json, res_header = RunMethod.run_main("GET", url, header=TestLogin.header)
    public_assert(res_json)
    data = jsonpath.jsonpath(res_json, "$.data")
    pytest.assume(data is not None)


@allure.step("查询token是否有效接口")
def get_token_valid():
    url = host + f"/service-user/token/valid"
    res_json, res_header = RunMethod.run_main("GET", url, header=TestLogin.header)
    public_assert(res_json)


@allure.feature("不同账号的登录测试")
@allure.testcase("http://132.232.109.76/zentao/testcase-view-24250-1.html")
class TestLogin:

    header = {"Content-Type": "application/json;charset=UTF-8",
              "Authorization": "default"}

    @allure.story("测试登录")
    @pytest.mark.parametrize("body_data", data_config.login_data)
    def test_login(self, body_data):
        token = jyy_login(body_data)
        TestLogin.header["Authorization"] = "Bearer " + token
        employee_id, employee_name = get_employee_info(token)
        get_employee_module(employee_id)
        get_token_valid()

