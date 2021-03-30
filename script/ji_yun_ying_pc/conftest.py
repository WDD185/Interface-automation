from common.run_method import RunMethod
from script.ji_yun_ying_pc import common_config
from script.common_config import host
import pytest
import jsonpath

# 1.conftest中fixture的scope参数为session，那么所有的测试文件执行前执行一次
# 2.conftest中fixture的scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
# 3.conftest中fixture的scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
# 4.conftest中fixture的scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture


@pytest.fixture(scope="session", autouse=True)
def ji_yun_ying_login():
    url = host + "/service-user/auth/employee"
    body_data = common_config.login_data
    res_json, res_header = RunMethod.run_main("POST", url, body_data=body_data, header=common_config.header)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    if tokens:
        common_config.header.setdefault("Authorization", f"Bearer {tokens[0]}", )
    else:
        common_config.header.setdefault("Authorization", "token  not found")


# def pytest_collection_modifyitems(session, config, items):
#     print(dir(config))
#     print(dir(items[0]))





