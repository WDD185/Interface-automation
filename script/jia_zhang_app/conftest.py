from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure
import pytest


@allure.feature("登录家长pp")
@pytest.fixture(scope="session", autouse=True)
def login():
    print("家长app登录接口")
    return "---------"


