import allure
import pytest
import jsonpath
from script.base_api.service_statistics.statistics import statistics_advance_charge_receipt_post
from script.ji_yun_ying_pc.statistical_report.data_config import receipt_detail_data
from script import public_asserts
from script import public_asserts_api
from script.default_header import jyy_header


@allure.epic("测试收据明细报表")
@allure.feature("测试收据明细报表")
class TestReceiptDetail:

    @allure.story("测试收据明细报表")
    @allure.step("测试收据明细列表查询-关键字筛选")
    @pytest.mark.parametrize("keyword", receipt_detail_data.keywords)
    def test_list_search(self, keyword):
        keyword_value = keyword.get("keyword")
        body = {
            "pageNum": 1,
            "pageSize": 1000,
            "keyword": keyword_value,
            "startTime": "2021-04-06",
            "endTime": "2021-04-12",
            "schoolIds": receipt_detail_data.school_areas,
            "receiptType": ["ORDER", "REFUND", "CARRYOVER", "CLASS_CHANGE_IN", "CLASS_CHANGE_OUT"],
            "schoolAreaType": "收费"
        }
        res = statistics_advance_charge_receipt_post(body=body, header=jyy_header)
        keyword_type = keyword.get("keyword_type")
        if keyword_type == "student_name":
            student_names = jsonpath.jsonpath(res, "$.data.list..studentName")
            result = public_asserts.assert_res_field_contain_value(student_names, keyword_value)
            pytest.assume(result)
        elif keyword_type == "receipt":
            receipts = jsonpath.jsonpath(res, "$.data.list..orderNo")
            result = public_asserts.assert_res_field_equal_value(receipts, keyword_value)
            pytest.assume(result)
        else:
            student_ids = jsonpath.jsonpath(res, "$.data.list..studentId")
            result = public_asserts_api.assert_phone_search(student_ids, keyword_value)
            pytest.assume(result)

