from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure
import pytest

# 1.conftest中fixture的scope参数为session，那么所有的测试文件执行前执行一次
# 2.conftest中fixture的scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
# 3.conftest中fixture的scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
# 4.conftest中fixture的scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture


# @allure.feature("极运营登录")
@pytest.fixture()
@allure.story("极运营登录接口")
def ji_yun_ying_login():
    url = data_config.host + "/service-user/auth/employee"
    body_data = data_config.login_data[0]
    res_json, res_header = RunMethod.run_main("POST", url, body_data=body_data, header=data_config.header)
    print("登录极运营")
    assert res_json.get("code", "-1") == 0
    return "token"



