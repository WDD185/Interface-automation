
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/订单/计算订单总价(旧)")
def app_order_countOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/countOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/报名/app端获取可使用优惠及优惠券")
def app_order_queryMatchDiscountAndCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/queryMatchDiscountAndCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/计算订单总价")
def app_order_calculateOrderPrice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/calculateOrderPrice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/提交作业")
def app_homework_submit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework/submit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/获取学生提交的作业")
def app_homework_studentHomework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework/studentHomework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业图片上传")
def app_upload_homework_img_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/upload/homework/img"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业附件上传")
def app_upload_homework_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/upload/homework/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/学生作业排行榜")
def app_homework_rankingList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework/rankingList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/资源/App根据视频主键查询视频真实地址")
def app_src_getSrcInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/src/getSrcInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/新增订单")
def app_order_saveOrder_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/saveOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/订单")
def app_order_queryOrderGeneralForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/queryOrderGeneralForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/订单/查询订单详情")
def app_order_queryOrderDetailForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/queryOrderDetailForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券/根据优惠券查询学生可报名班级")
def app_coupon_couponForAppClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/coupon/couponForAppClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/报名/app端下单前的预验证")
def app_order_preValidOrderCondition_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/preValidOrderCondition"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/未读数量")
def app_homework_unread_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework/unread"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/数据导入接口")
def app_exam_excel_insertDataSource_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/excel/insertDataSource"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/成绩报告列表查询（筛选）")
def app_exam_getTestList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/getTestList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/多科详情")
def app_exam_multiSectionDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/multiSectionDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/单科详情-成绩")
def app_exam_singleSectionDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/singleSectionDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/考试知识点")
def app_exam_knowPointDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/knowPointDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/题目")
def app_exam_topicDetail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/topicDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/首页未读小红点")
def app_exam_unRead_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/unRead"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家长端App/分享")
def app_exam_share_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/exam/share"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表")
def app_class_studentId_student_allowable_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/class/{studentId}/student/allowable"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询班级座次")
def app_classes_classId_seats_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classes/{classId}/seats"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴列表")
def app_classfeedback_student_notes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classfeedback/student/notes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/删除某个学生购课单中的某一条记录")
def app_purchaseOrder_purchaseId_studentstudentId_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{purchaseId}/student{studentId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/获取手机号码登录验证码")
def app_external_login_phoneNumber_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/external/login/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取同大区下的所有校区")
def app_class_schoolAreaId_getSameLevelSchoolArea_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/class/{schoolAreaId}/getSameLevelSchoolArea"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生已经报的班级")
def app_classes_reading_student_studentId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classes/reading/student/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改当前学生用户一个或多个基础属性值")
def app_student_studentId_attribute_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/attribute"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/判断学生将要报名的课程和已经报名的课程是否有排课冲突")
def app_student_studentId_class_Conflict_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/class/Conflict"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/某个学生向购课单中添加课程")
def app_purchaseOrder_studentId_student_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/某个学生用户主动发起调课请求")
def app_student_studentId_transferringClass_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/transferringClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码")
def app_user_studentId_backupMobilePhone_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/user/{studentId}/backupMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/删除用户设备绑定关系")
def app_pushRelationship_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/pushRelationship"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业详情")
def app_homework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个课程总的调课次数")
def app_transferred_classId_class_totalNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/transferred/{classId}/class/totalNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取授课老师信息")
def app_classes_teacher_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classes/teacher"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取手机验证码")
def app_external_phoneNumber_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/external/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个课程的某一讲能够调入的班级和讲次")
def app_transferred_classId_class_classScheduleId_section_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/transferred/{classId}/class/{classScheduleId}/section"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况")
def app_performances_details_studentId_student_classes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/performances/details/{studentId}/student/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/刷新校区缓存")
def app_class_refreshSchoolIdCache_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/class/refreshSchoolIdCache"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的某一个班级的详细信息")
def app_class_classId_alternative_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/class/{classId}/alternative/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中的课程")
def app_purchaseOrder_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中课程总数")
def app_purchaseOrder_studentId_student_count_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{studentId}/student/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表的筛选条件")
def app_class_selection_elective_Courses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/class/selection/elective/Courses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的详细列表")
def app_classes_studentId_student_unfinished_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classes/{studentId}/student/unfinished"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量修改某个学生购课单中多条记录的状态")
def app_purchaseOrder_studentId_student_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴详情")
def app_classfeedback_student_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classfeedback/student/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业列表")
def app_homeworks_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homeworks"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取学生用户的班帖列表所包含的属性")
def app_courseNote_field_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/courseNote/field"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/校验手机验证码")
def app_external_phoneNumber_validity_verificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/external/{phoneNumber}/validity/verificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改当前学生用户的基础属性值")
def app_student_studentId_attribute_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/attribute"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生未读班贴的数量")
def app_classes_unattended_student_studentId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classes/unattended/student/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生基本信息")
def app_student_studentId_basicInfo_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/basicInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生的续报类型")
def app_student_studentId_signUpType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/signUpType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/向校长信箱反馈问题")
def app_feedback_mailbox_studentId_student_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/feedback/mailbox/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/新增用户设备绑定关系")
def app_pushRelationship_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/pushRelationship"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的班级行课进度情况")
def app_classes_progress_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classes/progress/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题")
def app_feedback_mailbox_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/feedback/mailbox"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题上传的图片")
def app_feedback_feedbackId_mailbox_picture_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/feedback/{feedbackId}/mailbox/picture"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取用户登录的手机号码所绑定的所有学生")
def app_students_phoneNumber_mobilePhoneNumberBounding_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/students/{phoneNumber}/mobilePhoneNumberBounding"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/修改某个学生购课单中某一条记录的状态")
def app_purchaseOrder_purchaseId_student_studentId_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{purchaseId}/student/{studentId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取系统时间")
def app_public_systemCurrentTime_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/public/systemCurrentTime"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量删除某个学生购课单中的多条记录")
def app_purchaseOrder_studentId_student_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱反馈问题的反馈类型")
def app_feedbackType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/feedbackType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录密码")
def app_user_type_signInPassword_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/user/{type}/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/刷新班级缓存")
def app_class_refreshCache_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/class/refreshCache"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询学生是否有待支付订单")
def app_student_studentId_queryIsPayingOrder_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/queryIsPayingOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生具体某堂课的班帖详情")
def app_classfeedback_classId_class_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classfeedback/{classId}/class/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/使用手机验证码登录")
def app_login_verificationCode_receiveVerificationCode_studentPhoneNum_phoneNumber_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/login/{verificationCode}/receiveVerificationCode/{studentPhoneNum}/phoneNumber"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生电子账户")
def app_student_studentId_electronicAccount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/student/{studentId}/electronicAccount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码")
def app_user_studentId_bindingMobilePhone_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/user/{studentId}/bindingMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取未读班贴数量")
def app_classfeedback_student_unread_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/classfeedback/student/unread/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/基础/用户登录")
def app_auth_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/app/auth"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询某班是否有效可报名")
def app_classes_studentId_queryIsEffectiveClasses_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/app/classes/{studentId}/queryIsEffectiveClasses"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询某班是否设置教室以及所在校区是否支持选座")
def app_classes_isSupportChooseSeat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/app/classes/isSupportChooseSeat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/就读学校名查询")
def app_setting_query_school_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/app/setting/query/school"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/查询订单状态")
def app_order_queryStatus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/queryStatus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/释放座位")
def app_order_cancle_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/cancle/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/验证学生重复生成订单")
def app_order_studentHasOrder_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/studentHasOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单1/查询订单状态1")
def app_order_queryTest_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/queryTest"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/预占座位")
def app_order_take_seat_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/take/seat"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/报名/获取可使用优惠")
def app_order_discounts_queryMatchDiscount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/discounts/queryMatchDiscount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/订单状态修改")
def app_order_updateStatus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/updateStatus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/文件上传/头像上传")
def app_file_avatar_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/file/avatar"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/通过类别获取消息")
def app_notice_studentId_student_noticeTypeId_noticeType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/{studentId}/student/{noticeTypeId}/noticeType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询接收者某类消息")
def app_notice_belongId_belong_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/{belongId}/belong/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/文件上传/Base64上传")
def app_file_base64_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/file/base64"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询接收者消息类别")
def app_notice_belong_studentId_student_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/belong/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询某人的消息数量")
def app_notice_studentId_student_count_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/{studentId}/student/count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/消息通知/查询消息阅读状态")
def app_notice_student_studentId_readingState_put(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/student/{studentId}/readingState"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/新增订单(旧)")
def app_order_save_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/save"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/查询订单")
def app_order_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单管理/二维码查询订单")
def app_order_qr_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/qr/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/班帖/班帖列表")
def app_course_notes_stickerList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course-notes/stickerList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/班帖/班级列表")
def app_course_notes_queryClassList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course-notes/queryClassList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/班帖/查看新班帖详情")
def app_course_notes_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course-notes/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券张数")
def app_coupon_countValidCouponItemByStudentIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/coupon/countValidCouponItemByStudentIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券/优惠券列表")
def app_coupon_selectCouponItemsByStudentIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/coupon/selectCouponItemsByStudentIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端App/精品班帖/班帖详情")
def app_excellentNote_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/excellentNote/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端App/v1/班级列表")
def app_queryClassList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/queryClassList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端App/班帖未读小红点")
def app_excellentNote_student_unread_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/excellentNote/student/unread/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/优惠券/优惠券详情")
def app_coupon_selectCouponItemByIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/coupon/selectCouponItemByIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/订单/获取可使用优惠券")
def app_coupon_queryMatchCoupon_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/coupon/queryMatchCoupon"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/APP/查询可报班级/")
def app_classInfo_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/app/classInfo/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业列表")
def app_homework_homeworkList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework/homeworkList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业详情")
def app_homework_homeworkDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/homework/homeworkDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/计算促销活动价格")
def app_order_calculatePromotion_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_order/app/order/calculatePromotion"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单列表")
def app_purchaseOrder_getPurchaseOrderList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/purchaseOrder/getPurchaseOrderList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/我的/电子钱包余额")
def app_financial_epayDeductionByStudentIdForApp_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/app/financial/epayDeductionByStudentIdForApp"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/班级详情")
def app_course_getStudentClassDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/getStudentClassDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/课程提醒信息")
def app_course_courseNoticeMessage_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/courseNoticeMessage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程表/课程日期表")
def app_course_getCourseDateTable_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/getCourseDateTable"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程表/课次列表")
def app_course_listCourseTableSchedules_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/listCourseTableSchedules"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/班级列表")
def app_course_listStudentClasses_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/listStudentClasses"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/预习资料详情")
def app_geekMaterial_getPrepareMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/getPrepareMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/获取时间戳签名")
def app_geekMaterial_getTimestampSign_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/getTimestampSign"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/辅导资料详情")
def app_geekMaterial_getTutorialMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/getTutorialMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/资料下载列表")
def app_geekMaterial_listDownloadMaterials_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/listDownloadMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/预习资料列表")
def app_geekMaterial_listPrepareMaterials_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/listPrepareMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/分享资料下载列表")
def app_geekMaterial_listSharedMaterials_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/listSharedMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/辅导资料列表")
def app_geekMaterial_listTutorialMaterials_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/listTutorialMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端APP公共功能/获取当前时间")
def app_getTimestamp_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/getTimestamp"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/获取神策设备ID")
def app_sa_trackSensorsUser_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/sa/trackSensorsUser"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/添加视频学习记录")
def app_geekMaterial_addPrepareVideoStudyLog_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/addPrepareVideoStudyLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/添加预习题目答题记录")
def app_geekMaterial_addPrepareQuestionStudyLog_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/geekMaterial/addPrepareQuestionStudyLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/学习报告/列表")
def app_learnReport_learnReportList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/learnReport/learnReportList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/学习报告/往期学习报告列表")
def app_learnReport_previousLearnReportList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/learnReport/previousLearnReportList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/学习报告/学习力走势折线统计")
def app_learnReport_learnPowerTrend_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/learnReport/learnPowerTrend"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/获取签名")
def app_getSignature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_src/app/getSignature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/获取视频签名")
def app_getVodSignature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_src/app/getVodSignature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("资源中心/获取cos签名")
def app_getPutSignature_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_src/app/getPutSignature"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/最近上课")
def app_course_recentClassTime_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/recentClassTime"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/系统消息")
def app_notice_change_status_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/change/status"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/未读条数")
def app_notice_unReadNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/unReadNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/班级列表(新)")
def app_course_newListStudentClasses_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/course/newListStudentClasses"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/用户转介绍金额")
def app_finance_introduce_user_amount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/app/finance/introduce/user/amount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/领取至电子钱包")
def app_finance_introduce_receive_receiveToWallet_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/app/finance/introduce/receive/receiveToWallet"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/电子钱包/流水")
def app_financial_wallet_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/app/financial/wallet/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/明细列表")
def app_finance_introduce_receive_introduced_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/app/finance/introduce/receive/introduced/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/转介绍/发放明细")
def app_finance_introduce_receive_query_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/app/finance/introduce/receive/query/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("未读消息条数")
def app_notice_countUnread_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/countUnread"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("消息设置为已读")
def app_notice_readNotice_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/readNotice"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("伯索--最近10分钟上课")
def app_notice_tenMin_send_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/app/notice/tenMin/send"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/双师/极构获取token")
def app_zeGou_getToken_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/zeGou/getToken"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/双师/获取班级当前排课")
def app_zeGou_queryClassesIsAvailableVideo_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/app/zeGou/queryClassesIsAvailableVideo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮app/所有消息未读数")
def app_notice_getNotReadCount_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_jksxb_app/app/notice/getNotReadCount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

