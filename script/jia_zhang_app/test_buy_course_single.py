from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure


@allure.feature("家长购课单")
class TestCourseSingle:

    @allure.story("查询购课单班级")
    def test_single_list(self, login):
        pass

    @allure.story("查询优惠信息")
    def test_search_discount(self, login):
        pass


