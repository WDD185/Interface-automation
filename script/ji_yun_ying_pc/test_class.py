from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure


@allure.feature("班级")
class TestClass:

    @allure.story("新建班级")
    def test_new_class(self, ji_yun_ying_login):
        print("新建班级", ji_yun_ying_login)
        assert 1 == 1

    @allure.story("编辑班级")
    def test_edit_class(self):
        print("编辑线索班级")
        assert 1 == 1


