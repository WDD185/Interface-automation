from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure
from script import common_config


@allure.feature("极运营app订单业务")
class TestOrder:

    @allure.story("极运营app选择学生")
    def test_search_student(self):
        print("极运营app选择学生")
        print(common_config.host)

    @allure.story("极运营app查询班级")
    def test_search_class(self):
        pass


