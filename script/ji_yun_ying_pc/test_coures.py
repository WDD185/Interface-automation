from common.run_method import RunMethod
from script.ji_yun_ying_pc import data_config
import allure


@allure.feature("课程")
class TestCourse:

    @allure.story("新建课程")
    def test_new_course(self):
        print("新建课程")
        assert 1 == 1

    @allure.story("编辑课程")
    def test_edit_course(self):
        print("编辑课程")
        assert 1 == 1


