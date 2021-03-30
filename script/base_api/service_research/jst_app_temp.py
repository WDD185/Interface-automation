
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极师通APP/点名/查询待补点名的记录")
def jst_app_attendances_report_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/attendances/report"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/学生作业查阅情况详情")
def jst_app_homework_readStatusOfStudentDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/readStatusOfStudentDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/获取学生提交的作业")
def jst_app_homework_studentHomework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/studentHomework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/批改作业")
def jst_app_homework_correctHomework_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/correctHomework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/用户管理/接收短信验证码")
def jst_app_external_phoneNumber_receiveVerificationCode_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/external/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/用户管理/修改密码")
def jst_app_user_employee_signinPassword_patch(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/user/employee/signinPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/教研/课件库/app段查询绑定教材")
def jst_app_research_update_getVersionNameByTeacherIdToHomeWork_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/update/getVersionNameByTeacherIdToHomeWork"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/首页/获取老师课程表")
def jst_app_schedules_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/schedules"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/获取点名名单")
def jst_app_attendances_members_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/attendances/members"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/基础/极师通用户登录")
def jst_app_auth_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/jst-app/auth"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/通过接收者ID获取消息")
def jst_app_notice_receiverId_student_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/jst-app/notice/{receiverId}/student"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/查询老师在目前所教的班级")
def jst_app_teachers_teacherId_classes_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/teachers/{teacherId}/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/查询老师在某个时间段内的排课计划")
def jst_app_teachers_teacherId_timetables_queries_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/teachers/{teacherId}/timetables/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/获取用户信息")
def jst_app_employees_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_user/jst-app/employees/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/待发送班帖列表查询")
def jst_app_excellent_notes_findUnpublishedNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/excellent-notes/findUnpublishedNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/已发送班帖列表")
def jst_app_excellent_notes_publishedNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/excellent-notes/publishedNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/已发送班帖查阅")
def jst_app_excellent_notes_readNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/excellent-notes/readNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/班帖详情")
def jst_app_excellent_notes_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/excellent-notes/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/编辑班帖")
def jst_app_excellent_notes_courseNoteId_publishNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/excellent-notes/{courseNoteId}/publishNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/上传补点名凭证")
def jst_app_upload_attendance_img_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/jst-app/upload/attendance/img"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/发布作业")
def jst_app_homework_publishHomework_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/publishHomework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/作业列表")
def jst_app_homework_homeworkList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/homeworkList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/班级列表")
def jst_app_homework_myClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/myClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/学生作业查阅情况")
def jst_app_homework_readStatusOfStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/readStatusOfStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/作业详情")
def jst_app_homework_homeworkDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/homeworkDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/删除作业")
def jst_app_homework_delHomework_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/delHomework"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/提交（或修改）点名数据")
def jst_app_attendances_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/attendances"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/教研/备课/查询老师及教材版本")
def jst_app_classes_getVersionNameByTeacherId_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_education/jst-app/classes/getVersionNameByTeacherId"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/教研/课件库/讲次查询")
def jst_app_research_textbook_courseContent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/textbook/courseContent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/教研/课件库/讲次和课件")
def jst_app_research_textbook_getCoursewareList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/textbook/getCoursewareList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/补点名")
def jst_app_attendances_supply_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/attendances/supply"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页感叹号")
def jst_app_status_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/status"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/图片文件上传")
def jst_app_upload_homework_img_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/jst-app/upload/homework/img"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/其他文件上传")
def jst_app_upload_homework_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/jst-app/upload/homework/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极客数学帮(家长APP)/通用/文件上传")
def jst_app_file_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/jst-app/file"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App撤回作业")
def jst_app_homework_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/获取班级与课次")
def jst_app_homework_classIndex_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/jst-app/homework/classIndex"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/我的教材")
def jst_app_research_update_getVersionNameByTeacherId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/update/getVersionNameByTeacherId"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/讲次下课件")
def jst_app_research_textbook_courseware_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/textbook/courseware"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/讲次下总数及阅读数")
def jst_app_research_lectureFileReadStat_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/lectureFileReadStat"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/我的教案列表查询")
def jst_app_research_textbook_lessonPlans_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/textbook/lessonPlans"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/教案上传")
def jst_app_research_teaching_plan_submit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/teaching_plan/submit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/查阅")
def jst_app_research_textbook_checkRead_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/textbook/checkRead"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/根据讲次查询教案")
def jst_app_research_teaching_plan_current_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/teaching_plan/current/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/教案撤回")
def jst_app_research_teaching_plan_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/teaching_plan/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/app/教案删除")
def jst_app_research_teaching_plan_del_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_research/jst-app/research/teaching_plan/del"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

