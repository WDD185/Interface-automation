import pytest
from script import common_config
from script import db_config


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
