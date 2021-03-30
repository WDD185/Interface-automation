
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极数据/大屏/首页人次三率")
def big_screen_queryBigScreenIndexBussinessRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryBigScreenIndexBussinessRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/首页目标完成雷达图")
def big_screen_queryBigScreenIndexRadar_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryBigScreenIndexRadar"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/首页目标完成排行")
def big_screen_queryBigScreenIndexRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryBigScreenIndexRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/首页校区目标完成")
def big_screen_queryBigScreenIndexSchoolAchieveRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryBigScreenIndexSchoolAchieveRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/首页招生动态")
def big_screen_queryBigScreenIndexRange_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryBigScreenIndexRange"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/校区增长率")
def big_screen_querySchoolGrowingRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySchoolGrowingRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/单校规模同比")
def big_screen_querySchoolScaleYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySchoolScaleYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/单校规模环比")
def big_screen_querySchoolScaleQuarterOnQuarter_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySchoolScaleQuarterOnQuarter"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级人次同比")
def big_screen_queryGradePersonTimeYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradePersonTimeYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级人次环比")
def big_screen_queryGradePersonTimeQuarterOnQuarter_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradePersonTimeQuarterOnQuarter"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目人次同比")
def big_screen_querySubjectPersonTimeYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectPersonTimeYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/课型人次同比")
def big_screen_queryCourseTypePersonTimeYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryCourseTypePersonTimeYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/课型人次占比")
def big_screen_queryCourseTypePersonTimeProportion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryCourseTypePersonTimeProportion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校退费率同比")
def big_screen_queryNewSchoolRefundYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolRefundYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校退费率排名")
def big_screen_queryNewSchoolRefundRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolRefundRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校满班率同比")
def big_screen_queryNewSchoolFullClassYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolFullClassYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校满班率排名")
def big_screen_queryNewSchoolFullClassRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolFullClassRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校续报率同比")
def big_screen_queryNewSchoolContinueYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolContinueYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校续报率排名")
def big_screen_queryNewSchoolContinueRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolContinueRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校人次同比")
def big_screen_queryNewSchoolPersonTimeYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolPersonTimeYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校人次排名")
def big_screen_queryNewSchoolPersonTimeRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolPersonTimeRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/新开校汇总")
def big_screen_queryNewSchoolAllCount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryNewSchoolAllCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/最近更新时间")
def big_screen_queryLastUpdateTime_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryLastUpdateTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/入口年级人次占比同比")
def big_screen_queryEntryPersonTimeProportion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryEntryPersonTimeProportion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/入口年级单校规模排行榜")
def big_screen_queryEntrySchoolScaleRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryEntrySchoolScaleRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/入口年级退费率")
def big_screen_queryEntryRefundRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryEntryRefundRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/入口年级满班率")
def big_screen_queryEntryFullClassRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryEntryFullClassRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/入口年级报率")
def big_screen_queryEntryContinueRate_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryEntryContinueRate"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/通用条件（班型，校区类型）")
def big_screen_queryCommonInfo_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryCommonInfo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目带班量·同比")
def big_screen_querySubjectTeacherClassCountYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectTeacherClassCountYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/学段带班量·同比")
def big_screen_queryPhaseTeacherClassCountYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryPhaseTeacherClassCountYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/带班量排名")
def big_screen_queryTeacherClassCountRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryTeacherClassCountRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目满班率·同比")
def big_screen_querySubjectFullClassYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectFullClassYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级满班率·同比")
def big_screen_queryGradeFullClassYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradeFullClassYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/满班率排名")
def big_screen_queryFullClassRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryFullClassRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/续报率排名")
def big_screen_queryContinueRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryContinueRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/优生公立校分布")
def big_screen_queryTopStudentSchoolDistribution_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryTopStudentSchoolDistribution"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/优生概览")
def big_screen_queryTopStudentCount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryTopStudentCount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/优生占比排行榜")
def big_screen_queryTopStudentRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryTopStudentRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目优生占比同比")
def big_screen_querySubjectTopStudentProportion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectTopStudentProportion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级优生占比同比")
def big_screen_queryGradeTopStudentProportion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradeTopStudentProportion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/续报率折线图")
def big_screen_queryContinueRange_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryContinueRange"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/退费率原因占比")
def big_screen_queryRefundReasonProportion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryRefundReasonProportion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/退费率排名")
def big_screen_queryRefundRank_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryRefundRank"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目退费率·同比")
def big_screen_querySubjectRefundYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectRefundYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级退费率·同比")
def big_screen_queryGradeRefundYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradeRefundYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级续报率&退费率")
def big_screen_queryGradeContinueAndRefund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradeContinueAndRefund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目续报率&退费率")
def big_screen_querySubjectContinueAndRefund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectContinueAndRefund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级优生续报率·同比")
def big_screen_queryGradeTopContinueYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradeTopContinueYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目续报率·同比")
def big_screen_querySubjectContinueYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectContinueYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/年级续报率·同比")
def big_screen_queryGradeContinueYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/queryGradeContinueYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极数据/大屏/科目优生续报率·同比")
def big_screen_querySubjectTopContinueYearOnYear_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_web/big-screen/querySubjectTopContinueYearOnYear"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

