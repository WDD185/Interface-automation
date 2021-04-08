import pytest
from script import common_config
from script import db_config
import jsonpath
from script import default_header
from script.base_api.service_user.auth import auth_employee_post


def pytest_addoption(parser):
    # 注册一个命令行选项host
    parser.addoption("--host", default="https://yf1.jkwljy.com/", dest="env", help="set test run env")
    # 注册一个命令行选项db
    parser.addoption("--db", default="yf1", dest="db", help="set test database")


@pytest.fixture(scope='session', autouse=True)
def get_host(pytestconfig):
    # 初始化测试环境变量
    test_host = pytestconfig.getoption('--host')
    if test_host:
        common_config.host = test_host

    test_db = pytestconfig.getoption('--db')
    if test_db:
        test_db_config = db_config.db_configs.get(test_db)
        if test_db_config:
            common_config.db_config = test_db_config


@pytest.fixture(scope="session", autouse=True)
def ji_yun_ying_login():
    body_data = {
        "type": "employee",
        "identityType": 1,
        "ip": "0.0.0.0",
        "account": "15360956010",
        "password": "88888888",
        "assistant": False
    }
    res_json = auth_employee_post(body=body_data, header=default_header.jyy_header, default_assert=False)
    tokens = jsonpath.jsonpath(res_json, "$.data.token")
    if tokens:
        default_header.jyy_header.setdefault("Authorization", f"Bearer {tokens[0]}")
    else:
        default_header.jyy_header.setdefault("Authorization", "token  not found")
