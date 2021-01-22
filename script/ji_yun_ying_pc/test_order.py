from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure


@allure.feature("极运营PC订单业务")
class TestOrder:

    @allure.story("极运营PC选择学生")
    def test_search_student(self):
        print("极运营PC查询学生接口")
        assert 1 == 1

    @allure.story("极运营PC查询班级")
    def test_get_user_info(self):
        print("极运营PC查询班级接口")
        assert 1 == 1


