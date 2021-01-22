from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure
import pytest
from script import common_config


@allure.feature("CRM线索")
class TestCrm:

    @allure.story("新建线索")
    @pytest.mark.usefixtures("ji_yun_ying_app_login")
    @pytest.mark.run(order=4)
    def test_new_clue(self):
        print("新建线索")
        assert 1 == 1
        print(common_config.host)

    @allure.story("编辑线索1")
    @pytest.mark.run(order=3)
    def test_edit_clue1(self):
        print("编辑线索1")
        assert 1 == 1

    @allure.story("编辑线索2")
    @pytest.mark.run(order=2)
    def test_edit_clue2(self):
        print("编辑线索2")
        assert 1 == 1

    @allure.story("编辑线索3")
    @pytest.mark.run(order=1)
    def test_edit_clue3(self):
        print("编辑线索3")
        assert 1 == 1


