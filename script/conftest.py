import pytest
from script import common_config


def pytest_addoption(parser):
    # 注册一个命令行选项host
    parser.addoption("--host", default="https://yf1.jkwljy.com/", dest="env", help="set test run env")


@pytest.fixture(scope='session', autouse=True)
def get_host(pytestconfig):
    # 初始化测试环境变量
    common_config.host = pytestconfig.getoption('--host')
