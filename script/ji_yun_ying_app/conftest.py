from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure
import pytest


@allure.feature("登录极运营app")
@pytest.fixture()
def ji_yun_ying_app_login():
    print("极运营app登录接口")
    assert 1 == 1



