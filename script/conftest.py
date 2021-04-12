import pytest
import jsonpath
from script import default_header
from common.common_config import common_config
from script.db_config import db_configs
from script.base_api.service_user.auth import auth_employee_post
from script.defalut_account import accounts


def pytest_addoption(parser):
    # 注册一个命令行选项host
    parser.addoption("--host", default="https://yf1.jkwljy.com", dest="env", help="set test run env")
    # 注册一个命令行选项db
    parser.addoption("--db", default="yf1", dest="db", help="set test database")
    # 注册一个命令行选项account
    parser.addoption("--account", default="A", dest="account", help="set run default account group")


@pytest.fixture(scope='session', autouse=True)
def get_host(pytestconfig):
    # 初始化测试环境变量
    common_config["host"] = pytestconfig.getoption('--host')

    # 初始化测试数据库配置
    common_config["db_config"] = db_configs.get(pytestconfig.getoption('--db'))


@pytest.fixture(scope="session", autouse=True)
def ji_yun_ying_login(pytestconfig):
    account = accounts.get(pytestconfig.getoption('--account').upper())
    jyy_account = account.get("jyy_account")
    body_data = {
        "type": "employee",
        "identityType": 1,
        "ip": "0.0.0.0",
        "account": jyy_account.get("account"),
        "password": jyy_account.get("password"),
        "assistant": False
    }
    res_json = auth_employee_post(body=body_data, header=default_header.jyy_header, default_assert=False)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    if tokens:
        default_header.jyy_header.setdefault("Authorization", f"Bearer {tokens[0]}")
    else:
        default_header.jyy_header.setdefault("Authorization", "token  not found")


# def pytest_collection_modifyitems(session, config, items):
#     print(dir(config))
#     print(dir(items[0]))


# 1.conftest中fixture的scope参数为session，那么所有的测试文件执行前执行一次
# 2.conftest中fixture的scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
# 3.conftest中fixture的scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
# 4.conftest中fixture的scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture

