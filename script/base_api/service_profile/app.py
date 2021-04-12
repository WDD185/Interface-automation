
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极客数学帮(家长APP)/作业/提交作业")
def app_homework_submit_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/提交作业"
    url = f"/service-profile/app/homework/submit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/获取学生提交的作业")
def app_homework_studentHomework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/获取学生提交的作业"
    url = f"/service-profile/app/homework/studentHomework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/学生作业排行榜")
def app_homework_rankingList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/学生作业排行榜"
    url = f"/service-profile/app/homework/rankingList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/未读数量")
def app_homework_unread_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/未读数量"
    url = f"/service-profile/app/homework/unread"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/数据导入接口")
def app_exam_excel_insertDataSource_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/数据导入接口"
    url = f"/service-profile/app/exam/excel/insertDataSource"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/成绩报告列表查询（筛选）")
def app_exam_getTestList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/成绩报告列表查询（筛选）"
    url = f"/service-profile/app/exam/getTestList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/多科详情")
def app_exam_multiSectionDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/多科详情"
    url = f"/service-profile/app/exam/multiSectionDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/单科详情-成绩")
def app_exam_singleSectionDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/单科详情-成绩"
    url = f"/service-profile/app/exam/singleSectionDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/考试知识点")
def app_exam_knowPointDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/考试知识点"
    url = f"/service-profile/app/exam/knowPointDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/题目")
def app_exam_topicDetail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/题目"
    url = f"/service-profile/app/exam/topicDetail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家長端App/首页未读小红点")
def app_exam_unRead_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家長端App/首页未读小红点"
    url = f"/service-profile/app/exam/unRead"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/家长端App/分享")
def app_exam_share_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "/家长端App/分享"
    url = f"/service-profile/app/exam/share"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表")
def app_class_studentId_student_allowable_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表"
    url = f"/service-profile/app/class/{studentId}/student/allowable"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询班级座次")
def app_classes_classId_seats_get(classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/查询班级座次"
    url = f"/service-profile/app/classes/{classId}/seats"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴列表")
def app_classfeedback_student_notes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生班贴列表"
    url = f"/service-profile/app/classfeedback/student/notes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/删除某个学生购课单中的某一条记录")
def app_purchaseOrder_purchaseId_studentstudentId_delete(purchaseId, studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/删除某个学生购课单中的某一条记录"    
    url = f"/service-profile/app/purchaseOrder/{purchaseId}/student{studentId}"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/获取手机号码登录验证码")
def app_external_login_phoneNumber_receiveVerificationCode_get(phoneNumber, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/获取手机号码登录验证码"
    url = f"/service-profile/app/external/login/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取同大区下的所有校区")
def app_class_schoolAreaId_getSameLevelSchoolArea_get(schoolAreaId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取同大区下的所有校区"
    url = f"/service-profile/app/class/{schoolAreaId}/getSameLevelSchoolArea"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生已经报的班级")
def app_classes_reading_student_studentId_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生已经报的班级"
    url = f"/service-profile/app/classes/reading/student/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改当前学生用户一个或多个基础属性值")
def app_student_studentId_attribute_put(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/修改当前学生用户一个或多个基础属性值"    
    url = f"/service-profile/app/student/{studentId}/attribute"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/判断学生将要报名的课程和已经报名的课程是否有排课冲突")
def app_student_studentId_class_Conflict_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/判断学生将要报名的课程和已经报名的课程是否有排课冲突"
    url = f"/service-profile/app/student/{studentId}/class/Conflict"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/某个学生向购课单中添加课程")
def app_purchaseOrder_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/某个学生向购课单中添加课程"
    url = f"/service-profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/某个学生用户主动发起调课请求")
def app_student_studentId_transferringClass_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/某个学生用户主动发起调课请求"
    url = f"/service-profile/app/student/{studentId}/transferringClass"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码")
def app_user_studentId_backupMobilePhone_patch(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/修改用户登录绑定的备用手机号码"
    url = f"/service-profile/app/user/{studentId}/backupMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/删除用户设备绑定关系")
def app_pushRelationship_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/删除用户设备绑定关系"    
    url = f"/service-profile/app/pushRelationship"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业详情")
def app_homework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/作业详情"
    url = f"/service-profile/app/homework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个课程总的调课次数")
def app_transferred_classId_class_totalNum_get(classId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个课程总的调课次数"
    url = f"/service-profile/app/transferred/{classId}/class/totalNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取授课老师信息")
def app_classes_teacher_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取授课老师信息"
    url = f"/service-profile/app/classes/teacher"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取手机验证码")
def app_external_phoneNumber_receiveVerificationCode_get(phoneNumber, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取手机验证码"
    url = f"/service-profile/app/external/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个课程的某一讲能够调入的班级和讲次")
def app_transferred_classId_class_classScheduleId_section_get(classId, classScheduleId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个课程的某一讲能够调入的班级和讲次"
    url = f"/service-profile/app/transferred/{classId}/class/{classScheduleId}/section"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况")
def app_performances_details_studentId_student_classes_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生所有班级的出席情况"
    url = f"/service-profile/app/performances/details/{studentId}/student/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/刷新校区缓存")
def app_class_refreshSchoolIdCache_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/刷新校区缓存"
    url = f"/service-profile/app/class/refreshSchoolIdCache"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的某一个班级的详细信息")
def app_class_classId_alternative_studentId_student_get(classId, studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的某一个班级的详细信息"
    url = f"/service-profile/app/class/{classId}/alternative/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中的课程")
def app_purchaseOrder_studentId_student_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/获取某个学生购课单中的课程"
    url = f"/service-profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单中课程总数")
def app_purchaseOrder_studentId_student_count_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/获取某个学生购课单中课程总数"
    url = f"/service-profile/app/purchaseOrder/{studentId}/student/count"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表的筛选条件")
def app_class_selection_elective_Courses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生用户可以报名的所有班级的列表的筛选条件"
    url = f"/service-profile/app/class/selection/elective/Courses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的详细列表")
def app_classes_studentId_student_unfinished_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的详细列表"
    url = f"/service-profile/app/classes/{studentId}/student/unfinished"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量修改某个学生购课单中多条记录的状态")
def app_purchaseOrder_studentId_student_put(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/批量修改某个学生购课单中多条记录的状态"    
    url = f"/service-profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("PUT", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生班贴详情")
def app_classfeedback_student_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生班贴详情"
    url = f"/service-profile/app/classfeedback/student/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业列表")
def app_homeworks_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/作业列表"
    url = f"/service-profile/app/homeworks"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取学生用户的班帖列表所包含的属性")
def app_courseNote_field_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取学生用户的班帖列表所包含的属性"
    url = f"/service-profile/app/courseNote/field"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/校验手机验证码")
def app_external_phoneNumber_validity_verificationCode_get(phoneNumber, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/校验手机验证码"
    url = f"/service-profile/app/external/{phoneNumber}/validity/verificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改当前学生用户的基础属性值")
def app_student_studentId_attribute_patch(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/修改当前学生用户的基础属性值"
    url = f"/service-profile/app/student/{studentId}/attribute"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生未读班贴的数量")
def app_classes_unattended_student_studentId_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生未读班贴的数量"
    url = f"/service-profile/app/classes/unattended/student/{studentId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生基本信息")
def app_student_studentId_basicInfo_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取学生基本信息"
    url = f"/service-profile/app/student/{studentId}/basicInfo"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生的续报类型")
def app_student_studentId_signUpType_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取学生的续报类型"
    url = f"/service-profile/app/student/{studentId}/signUpType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/向校长信箱反馈问题")
def app_feedback_mailbox_studentId_student_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/向校长信箱反馈问题"
    url = f"/service-profile/app/feedback/mailbox/{studentId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/新增用户设备绑定关系")
def app_pushRelationship_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/新增用户设备绑定关系"
    url = f"/service-profile/app/pushRelationship"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的班级行课进度情况")
def app_classes_progress_studentId_student_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/获取某个学生未完成课程的班级行课进度情况"
    url = f"/service-profile/app/classes/progress/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题")
def app_feedback_mailbox_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题"
    url = f"/service-profile/app/feedback/mailbox"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题上传的图片")
def app_feedback_feedbackId_mailbox_picture_get(feedbackId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取校长信箱中反馈的问题上传的图片"
    url = f"/service-profile/app/feedback/{feedbackId}/mailbox/picture"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取用户登录的手机号码所绑定的所有学生")
def app_students_phoneNumber_mobilePhoneNumberBounding_get(phoneNumber, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取用户登录的手机号码所绑定的所有学生"
    url = f"/service-profile/app/students/{phoneNumber}/mobilePhoneNumberBounding"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/修改某个学生购课单中某一条记录的状态")
def app_purchaseOrder_purchaseId_student_studentId_patch(purchaseId, studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/修改某个学生购课单中某一条记录的状态"
    url = f"/service-profile/app/purchaseOrder/{purchaseId}/student/{studentId}"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取系统时间")
def app_public_systemCurrentTime_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取系统时间"
    url = f"/service-profile/app/public/systemCurrentTime"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/批量删除某个学生购课单中的多条记录")
def app_purchaseOrder_studentId_student_delete(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/批量删除某个学生购课单中的多条记录"    
    url = f"/service-profile/app/purchaseOrder/{studentId}/student"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取校长信箱反馈问题的反馈类型")
def app_feedbackType_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取校长信箱反馈问题的反馈类型"
    url = f"/service-profile/app/feedbackType"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录密码")
def app_user_type_signInPassword_patch(type, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/修改用户登录密码"
    url = f"/service-profile/app/user/{type}/signInPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/刷新班级缓存")
def app_class_refreshCache_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/刷新班级缓存"
    url = f"/service-profile/app/class/refreshCache"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课/查询学生是否有待支付订单")
def app_student_studentId_queryIsPayingOrder_post(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课/查询学生是否有待支付订单"
    url = f"/service-profile/app/student/{studentId}/queryIsPayingOrder"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取学生具体某堂课的班帖详情")
def app_classfeedback_classId_class_studentId_student_get(classId, studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课班帖/获取学生具体某堂课的班帖详情"
    url = f"/service-profile/app/classfeedback/{classId}/class/{studentId}/student"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/使用手机验证码登录")
def app_login_verificationCode_receiveVerificationCode_studentPhoneNum_phoneNumber_get(verificationCode, studentPhoneNum, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/使用手机验证码登录"
    url = f"/service-profile/app/login/{verificationCode}/receiveVerificationCode/{studentPhoneNum}/phoneNumber"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/获取学生电子账户")
def app_student_studentId_electronicAccount_get(studentId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/获取学生电子账户"
    url = f"/service-profile/app/student/{studentId}/electronicAccount"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码")
def app_user_studentId_bindingMobilePhone_patch(studentId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户管理/修改用户登录绑定的手机号码"
    url = f"/service-profile/app/user/{studentId}/bindingMobilePhone"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户行课班帖/获取未读班贴数量")
def app_classfeedback_student_unread_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户行课班帖/获取未读班贴数量"
    url = f"/service-profile/app/classfeedback/student/unread/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/班帖/班帖列表")
def app_course_notes_stickerList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/班帖/班帖列表"
    url = f"/service-profile/app/course-notes/stickerList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/班帖/班级列表")
def app_course_notes_queryClassList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/班帖/班级列表"
    url = f"/service-profile/app/course-notes/queryClassList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/班帖/查看新班帖详情")
def app_course_notes_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/班帖/查看新班帖详情"
    url = f"/service-profile/app/course-notes/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端App/精品班帖/班帖详情")
def app_excellentNote_detail_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长端App/精品班帖/班帖详情"
    url = f"/service-profile/app/excellentNote/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端App/v1/班级列表")
def app_queryClassList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长端App/v1/班级列表"
    url = f"/service-profile/app/queryClassList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长端App/班帖未读小红点")
def app_excellentNote_student_unread_note_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长端App/班帖未读小红点"
    url = f"/service-profile/app/excellentNote/student/unread/note"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业列表")
def app_homework_homeworkList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/作业列表"
    url = f"/service-profile/app/homework/homeworkList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/作业/作业详情")
def app_homework_homeworkDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/作业/作业详情"
    url = f"/service-profile/app/homework/homeworkDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/用户购课单/获取某个学生购课单列表")
def app_purchaseOrder_getPurchaseOrderList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/用户购课单/获取某个学生购课单列表"
    url = f"/service-profile/app/purchaseOrder/getPurchaseOrderList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/班级详情")
def app_course_getStudentClassDetail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程/班级详情"
    url = f"/service-profile/app/course/getStudentClassDetail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/课程提醒信息")
def app_course_courseNoticeMessage_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程/课程提醒信息"
    url = f"/service-profile/app/course/courseNoticeMessage"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程表/课程日期表")
def app_course_getCourseDateTable_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程表/课程日期表"
    url = f"/service-profile/app/course/getCourseDateTable"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程表/课次列表")
def app_course_listCourseTableSchedules_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程表/课次列表"
    url = f"/service-profile/app/course/listCourseTableSchedules"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/班级列表")
def app_course_listStudentClasses_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程/班级列表"
    url = f"/service-profile/app/course/listStudentClasses"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/预习资料详情")
def app_geekMaterial_getPrepareMaterial_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/预习资料详情"
    url = f"/service-profile/app/geekMaterial/getPrepareMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/获取时间戳签名")
def app_geekMaterial_getTimestampSign_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/获取时间戳签名"
    url = f"/service-profile/app/geekMaterial/getTimestampSign"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/辅导资料详情")
def app_geekMaterial_getTutorialMaterial_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/辅导资料详情"
    url = f"/service-profile/app/geekMaterial/getTutorialMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/资料下载列表")
def app_geekMaterial_listDownloadMaterials_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/资料下载列表"
    url = f"/service-profile/app/geekMaterial/listDownloadMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/预习资料列表")
def app_geekMaterial_listPrepareMaterials_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/预习资料列表"
    url = f"/service-profile/app/geekMaterial/listPrepareMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/分享资料下载列表")
def app_geekMaterial_listSharedMaterials_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/分享资料下载列表"
    url = f"/service-profile/app/geekMaterial/listSharedMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/辅导资料列表")
def app_geekMaterial_listTutorialMaterials_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/辅导资料列表"
    url = f"/service-profile/app/geekMaterial/listTutorialMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/极数据/获取神策设备ID")
def app_sa_trackSensorsUser_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极运营/极数据/获取神策设备ID"
    url = f"/service-profile/app/sa/trackSensorsUser"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/添加视频学习记录")
def app_geekMaterial_addPrepareVideoStudyLog_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/添加视频学习记录"
    url = f"/service-profile/app/geekMaterial/addPrepareVideoStudyLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/极客资料/添加预习题目答题记录")
def app_geekMaterial_addPrepareQuestionStudyLog_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/极客资料/添加预习题目答题记录"
    url = f"/service-profile/app/geekMaterial/addPrepareQuestionStudyLog"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/学习报告/列表")
def app_learnReport_learnReportList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/学习报告/列表"
    url = f"/service-profile/app/learnReport/learnReportList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/学习报告/往期学习报告列表")
def app_learnReport_previousLearnReportList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/学习报告/往期学习报告列表"
    url = f"/service-profile/app/learnReport/previousLearnReportList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/学习报告/学习力走势折线统计")
def app_learnReport_learnPowerTrend_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/学习报告/学习力走势折线统计"
    url = f"/service-profile/app/learnReport/learnPowerTrend"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/最近上课")
def app_course_recentClassTime_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程/最近上课"
    url = f"/service-profile/app/course/recentClassTime"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/课程/班级列表(新)")
def app_course_newListStudentClasses_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极客数学帮(家长APP)/课程/班级列表(新)"
    url = f"/service-profile/app/course/newListStudentClasses"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/双师/极构获取token")
def app_zeGou_getToken_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/双师/极构获取token"
    url = f"/service-profile/app/zeGou/getToken"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("JkyAPP/双师/获取班级当前排课")
def app_zeGou_queryClassesIsAvailableVideo_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "JkyAPP/双师/获取班级当前排课"
    url = f"/service-profile/app/zeGou/queryClassesIsAvailableVideo"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

