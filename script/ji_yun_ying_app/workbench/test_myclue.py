import allure
import pytest
import jsonpath
from datetime import datetime

from script import public_asserts
from script.base_api import clue_queryAll_post, clue_addClue_post, clue_dict_studentSource_queryNoAuth_get
from script.default_header import jyy_app_header
from script.public_asserts import assert_res_field_order, assert_res_field_contain_value
from script.ji_yun_ying_app.data_config.data_myclue import end_time, start_time, \
    generate_phone, generate_name, generate_intentionLevel, generate_sourceId, pg_data


@allure.epic('工作台')
@allure.feature('我的线索')
class TestMyClue:

    # @allure.title('新增线索-填写必填项')
    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize('phone', [generate_phone()])
    # @pytest.mark.parametrize('name', [generate_name()])
    # @pytest.mark.parametrize('intentionLevel', [generate_intentionLevel()])
    # @pytest.mark.parametrize('sourceId', [generate_sourceId()])
    # def test_add_clue_Required(self, phone, name, intentionLevel):
    #     print(phone)
    #     print(name)
    #     print(intentionLevel)
    #     body = {"studentName": name,
    #             "collectPerson": "王星皓3",
    #             "otherRemark": "",
    #             "intentionLevel": intentionLevel,
    #             "sourceId": 111,
    #             "studentSex": "",
    #             "contactInfo": phone,
    #             "contactType": "PHONE",
    #             "secondContactInfo": "",
    #             "secondContactType": "PHONE",
    #             "citys": [
    #                 "510000",
    #                 "510100"
    #             ],
    #             "schoolProvinceId": "510000",
    #             "schoolProvinceName": "四川省",
    #             "schoolCityId": "510100",
    #             "schoolCityName": "成都市",
    #             "schoolId": "",
    #             "schoolName": "",
    #             "classRank": "",
    #             "gradeRank": "",
    #             "recentScore": "",
    #             "parentsHope": "",
    #             "studyHabit": "",
    #             "sourceIdFirstName": "线上营销",
    #             "sourceIdSecondName": "网站",
    #             "testPaperUrls": "",
    #             "belong": "PERSON",
    #             "createSchoolAreaId": 3015,
    #             "city": "510100"}
    #     res = clue_addClue_post(body=body, header=jyy_app_header)
    #     print(res)
    #     code = res['code']
    #     msg = res['msg']
    #     print(code)
    #     print(msg)
    #     assert code == 0
    #     assert msg == '成功'

    @allure.title('新增线索-不填写必填项')
    def test_add_clue_noRequired(self):
        body = {"studentName": '',
                "collectPerson": "王星皓3",
                "otherRemark": "",
                "intentionLevel": '',
                "sourceId": 111,
                "studentSex": "",
                "contactInfo": '',
                "contactType": "PHONE",
                "secondContactInfo": "",
                "secondContactType": "PHONE",
                "citys": [
                    "510000",
                    "510100"
                ],
                "schoolProvinceId": "510000",
                "schoolProvinceName": "四川省",
                "schoolCityId": "510100",
                "schoolCityName": "成都市",
                "schoolId": "",
                "schoolName": "",
                "classRank": "",
                "gradeRank": "",
                "recentScore": "",
                "parentsHope": "",
                "studyHabit": "",
                "sourceIdFirstName": "线上营销",
                "sourceIdSecondName": "网站",
                "testPaperUrls": "",
                "belong": "PERSON",
                "createSchoolAreaId": 3015,
                "city": "510100"}
        res = clue_addClue_post(body=body, header=jyy_app_header)
        print(res)
        code = res['code']
        msg = res['msg']
        print(code)
        print(msg)
        assert code == 100110001
        result = '第一联系方式不能为空' in msg
        assert result == True

    @allure.title('新增线索-第一联系方式重复')
    @pytest.mark.parametrize('phone', pg_data())
    @pytest.mark.parametrize('name', pg_data())
    @pytest.mark.parametrize('intentionLevel', [generate_intentionLevel()])
    def test_existent_clue(self, phone, name, intentionLevel):
        print(intentionLevel)
        print(name[1])
        print(phone[4])
        body = {"studentName": name[1],
                "collectPerson": "王星皓3",
                "otherRemark": "",
                "intentionLevel": intentionLevel,
                "sourceId": 111,
                "studentSex": "",
                "contactInfo": phone[4],
                "contactType": "PHONE",
                "secondContactInfo": "",
                "secondContactType": "PHONE",
                "citys": [
                    "510000",
                    "510100"
                ],
                "schoolProvinceId": "510000",
                "schoolProvinceName": "四川省",
                "schoolCityId": "510100",
                "schoolCityName": "成都市",
                "schoolId": "",
                "schoolName": "",
                "classRank": "",
                "gradeRank": "",
                "recentScore": "",
                "parentsHope": "",
                "studyHabit": "",
                "sourceIdFirstName": "线上营销",
                "sourceIdSecondName": "网站",
                "testPaperUrls": "",
                "belong": "PERSON",
                "createSchoolAreaId": 3015,
                "city": "510100"}
        res = clue_addClue_post(body=body, header=jyy_app_header)
        print(res)
        code = res['code']
        msg = res['msg']
        print(code)
        print(msg)
        assert code == 100210006
        result = '线索已存在' in msg
        assert result == True

    @allure.title('新增线索-来源渠道验证')
    def test_clue_source_channel(self):
        print('来源渠道验证')
        body = {}
        res = clue_dict_studentSource_queryNoAuth_get(body=body, header=jyy_app_header)
        print(res)
        code = res['code']
        msg = res['msg']
        print(code)
        print(msg)
        assert code == 0
        assert msg == '成功'

    @allure.title('线索列表-默认线索数据来源')
    @pytest.mark.run(order=2)
    def test_data_source(self):
        body = {
            "pageNum": 1,
            "pageSize": 10,
            "belong": "PERSON",
            "orderType": "desc",
            "createSchoolAreaId": 3015,
            "status": "FOLLOWING",
            "orderField": "id"}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        msg = res['msg']
        print(total)
        print(code)
        if total == 0:
            assert code == 0
            assert msg == '成功'
        else:
            createPerson = jsonpath.jsonpath(res, "$.data.list..createPerson")
            print(createPerson)
            result = assert_res_field_contain_value(createPerson, '王星皓3')
            pytest.assume(result)

    @allure.title('线索列表-录入时间降序')
    def test_data_sort(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "create_time"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        createTime = jsonpath.jsonpath(res, "$.data.list..createTime")
        print(createTime)
        result = assert_res_field_order(createTime, 'desc')
        pytest.assume(result)

    @allure.title('线索列表-录入时间正序')
    def test_data_sort2(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "asc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "create_time"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        createTime = jsonpath.jsonpath(res, "$.data.list..createTime")
        print(createTime)
        result = assert_res_field_order(createTime, 'asc')
        pytest.assume(result)

    @allure.title('线索列表-末次跟进时间正序')
    def test_data_sort3(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "asc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "last_follow_time"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        lastFollowTime = jsonpath.jsonpath(res, "$.data.list..lastFollowTime")
        print(lastFollowTime)
        if None in lastFollowTime:
            ID = jsonpath.jsonpath(res, "$.data.list..id")
            result = assert_res_field_order(ID, 'desc')
            pytest.assume(result)
        else:
            result = assert_res_field_order(lastFollowTime, 'asc')
            pytest.assume(result)

    @allure.title('线索列表-末次跟进时间降序')
    def test_data_sort4(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "last_follow_time"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        lastFollowTime = jsonpath.jsonpath(res, "$.data.list..lastFollowTime")
        print(lastFollowTime)
        if None in lastFollowTime:
            ID = jsonpath.jsonpath(res, "$.data.list..id")
            result = assert_res_field_order(ID, 'desc')
            pytest.assume(result)
        else:
            result = assert_res_field_order(lastFollowTime, 'asc')
            pytest.assume(result)

    @allure.title('线索列表-计划跟进时间降序')
    def test_data_sort5(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "next_follow_time"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        nextFollowTime = jsonpath.jsonpath(res, "$.data.list..nextFollowTime")
        print(nextFollowTime)
        result = assert_res_field_order(nextFollowTime, 'desc')
        pytest.assume(result)

    @allure.title('线索列表-计划跟进时间降序')
    def test_data_sort6(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "asc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "next_follow_time"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        nextFollowTime = jsonpath.jsonpath(res, "$.data.list..nextFollowTime")
        print(nextFollowTime)
        result = assert_res_field_order(nextFollowTime, 'asc')
        pytest.assume(result)

    @allure.title('线索列表-未跟进线索筛选')
    def test_data_not_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "followingStatus": "UNFOLLOWED",
                "followingStatusLabel": "未跟进"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            statusTranslate = jsonpath.jsonpath(res, "$.data.list..statusTranslate")
            print(statusTranslate)
            result = assert_res_field_contain_value(statusTranslate, '未跟进')
            pytest.assume(result)

    @allure.title('线索列表-跟进中线索筛选')
    def test_data_in_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "followingStatus": "FOLLOWING",
                "followingStatusLabel": "跟进中"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            statusTranslate = jsonpath.jsonpath(res, "$.data.list..statusTranslate")
            print(statusTranslate)
            result = assert_res_field_contain_value(statusTranslate, '跟进中')
            pytest.assume(result)

    @allure.title('线索列表-已逾期线索筛选')
    def test_data_over_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "followingStatus": "OVERTIME",
                "followingStatusLabel": "已逾期"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            statusTranslate = jsonpath.jsonpath(res, "$.data.list..statusTranslate")
            print(statusTranslate)
            result = assert_res_field_contain_value(statusTranslate, '已逾期')
            pytest.assume(result)

    @allure.title('线索列表-S意向等级')
    def test_data_s_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "intentionLevel": "S",
                "intentionLevelLabel": "S（高意向）"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            intentionLevel = jsonpath.jsonpath(res, "$.data.list..intentionLevel")
            print(intentionLevel)
            result = assert_res_field_contain_value(intentionLevel, 'S')
            pytest.assume(result)

    @allure.title('线索列表-A意向等级')
    def test_data_a_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "intentionLevel": "A",
                "intentionLevelLabel": "A（中等意向）"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            intentionLevel = jsonpath.jsonpath(res, "$.data.list..intentionLevel")
            print(intentionLevel)
            result = assert_res_field_contain_value(intentionLevel, 'A')
            pytest.assume(result)

    @allure.title('线索列表-B意向等级')
    def test_data_b_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "intentionLevel": "B",
                "intentionLevelLabel": "B（低意向）"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            intentionLevel = jsonpath.jsonpath(res, "$.data.list..intentionLevel")
            print(intentionLevel)
            result = assert_res_field_contain_value(intentionLevel, 'B')
            pytest.assume(result)

    @allure.title('线索列表-C意向等级')
    def test_data_c_follow(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "intentionLevel": "C",
                "intentionLevelLabel": "C（无意向）"}

        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            intentionLevel = jsonpath.jsonpath(res, "$.data.list..intentionLevel")
            print(intentionLevel)
            result = assert_res_field_contain_value(intentionLevel, 'C')
            pytest.assume(result)

    @allure.title('线索列表-模糊查询')
    def test_fuzzy_query(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "studentName": "4",
                "status": "FOLLOWING",
                "orderField": "id"}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            studentName = jsonpath.jsonpath(res, "$.data.list..studentName")
            print(studentName)
            result = assert_res_field_contain_value(studentName, '4')
            pytest.assume(result)

    @allure.title('线索列表-电话号码查询')
    def test_num_query(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "studentName": "15588880033",
                "status": "FOLLOWING",
                "orderField": "id"}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            contactInfo = jsonpath.jsonpath(res, "$.data.list..contactInfo")
            print(contactInfo)
            result = assert_res_field_contain_value(contactInfo, '15588880033')
            pytest.assume(result)

    @allure.title('线索列表-多条件查询')
    def test_multiple_query(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "studentName": "4",
                "status": "FOLLOWING",
                "orderField": "id",
                "followingStatus": "OVERTIME",
                "intentionLevel": "A",
                "intentionLevelLabel": "A（中等意向）",
                "followingStatusLabel": "已逾期"}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            statusTranslate = jsonpath.jsonpath(res, "$.data.list..statusTranslate")
            intentionLevel = jsonpath.jsonpath(res, "$.data.list..intentionLevel")
            studentName = jsonpath.jsonpath(res, "$.data.list..studentName")
            print(studentName)
            print(statusTranslate)
            print(intentionLevel)
            result = assert_res_field_contain_value(studentName, '4')
            result1 = assert_res_field_contain_value(statusTranslate, '已逾期')
            result2 = assert_res_field_contain_value(intentionLevel, 'A')
            pytest.assume(result)
            pytest.assume(result1)
            pytest.assume(result2)

    @allure.title('线索列表-线索来源')
    def test_clue_source(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "sourceId": "100"}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            sourceName = jsonpath.jsonpath(res, "$.data.list..sourceName")
            print(sourceName)
            result = assert_res_field_contain_value(sourceName, '线上营销')
            pytest.assume(result)

    @allure.title('线索列表-年级')
    def test_class_level(self):
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "sourceId": '',
                "publicGrade": "三年级"}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            publicGrade = jsonpath.jsonpath(res, "$.data.list..publicGrade")
            print(publicGrade)
            result = assert_res_field_contain_value(publicGrade, '三年级')
            pytest.assume(result)

    @allure.title('线索列表-录入时间')
    @pytest.mark.parametrize("s_time", [start_time()])
    @pytest.mark.parametrize("e_time", [end_time()])
    def test_input_time(self, s_time, e_time):
        print(s_time)
        print(e_time)
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "createTimeBeginDateStr": s_time,
                "createTimeEndDateStr": e_time}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            createTimeStr = jsonpath.jsonpath(res, "$.data.list..createTimeStr")
            print(createTimeStr)
            ctime1 = max(createTimeStr)
            ct1 = datetime.strptime(ctime1, '%Y-%m-%d %H:%M:%S')
            ct3 = datetime.strftime(ct1, '%Y-%m-%d')
            ctime2 = min(createTimeStr)
            ct2 = datetime.strptime(ctime2, '%Y-%m-%d %H:%M:%S')
            ct4 = datetime.strftime(ct2, '%Y-%m-%d')
            print(ct3)
            print(ct4)
            assert s_time <= ct3 <= e_time
            assert s_time <= ct4 <= e_time

    @allure.title('线索列表-末次跟进时间时间')
    @pytest.mark.parametrize("s_time", [start_time()])
    @pytest.mark.parametrize("e_time", [end_time()])
    def test_last_follow_time(self, s_time, e_time):
        print(s_time)
        print(e_time)
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "lastFollowTimeBeginDateStr": s_time,
                "lastFollowTimeEndDateStr": e_time}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            lastFollowTimeStr = jsonpath.jsonpath(res, "$.data.list..lastFollowTimeStr")
            print(lastFollowTimeStr)
            ptime1 = max(lastFollowTimeStr)
            ptime2 = min(lastFollowTimeStr)
            print(ptime1)
            print(ptime2)
            assert s_time <= ptime1 <= e_time
            assert s_time <= ptime2 <= e_time

    @allure.title('线索列表-计划跟进时间')
    @pytest.mark.parametrize("s_time", [start_time()])
    @pytest.mark.parametrize("e_time", [end_time()])
    def test_next_follow_time(self, s_time, e_time):
        print(s_time)
        print(e_time)
        body = {"pageNum": 1,
                "pageSize": 10,
                "belong": "PERSON",
                "orderType": "desc",
                "createSchoolAreaId": 3015,
                "status": "FOLLOWING",
                "orderField": "id",
                "nextFollowTimeBeginDateStr": s_time,
                "nextFollowTimeEndDateStr": e_time}
        res = clue_queryAll_post(body=body, header=jyy_app_header)
        print(res)
        total = res['data']['total']
        code = res['code']
        print(code)
        print(total)
        if total == 0:
            assert code == 0
        else:
            nextFollowTimeStr = jsonpath.jsonpath(res, "$.data.list..nextFollowTimeStr")
            print(nextFollowTimeStr)
            ptime1 = max(nextFollowTimeStr)
            ptime2 = min(nextFollowTimeStr)
            print(ptime1)
            print(ptime2)
            assert s_time <= ptime1 <= e_time
            assert s_time <= ptime2 <= e_time
