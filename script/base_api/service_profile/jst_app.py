
from common.run_method import RunMethod
from script.public_asserts import public_assert
import pytest
import allure


@allure.step("极师通APP/点名/查询待补点名的记录")
def jst_app_attendances_report_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通APP/点名/查询待补点名的记录"
    url = f"/service-profile/jst-app/attendances/report"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/学生作业查阅情况详情")
def jst_app_homework_readStatusOfStudentDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/学生作业查阅情况详情"
    url = f"/service-profile/jst-app/homework/readStatusOfStudentDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/获取学生提交的作业")
def jst_app_homework_studentHomework_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/获取学生提交的作业"
    url = f"/service-profile/jst-app/homework/studentHomework"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/批改作业")
def jst_app_homework_correctHomework_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/批改作业"
    url = f"/service-profile/jst-app/homework/correctHomework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/用户管理/接收短信验证码")
def jst_app_external_phoneNumber_receiveVerificationCode_get(phoneNumber, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/用户管理/接收短信验证码"
    url = f"/service-profile/jst-app/external/{phoneNumber}/receiveVerificationCode"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("家长APP/用户管理/修改密码")
def jst_app_user_employee_signinPassword_patch(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "家长APP/用户管理/修改密码"
    url = f"/service-profile/jst-app/user/employee/signinPassword"
    res = RunMethod.run_request("PATCH", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/首页/获取老师课程表")
def jst_app_schedules_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通APP/首页/获取老师课程表"
    url = f"/service-profile/jst-app/schedules"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/获取点名名单")
def jst_app_attendances_members_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通APP/点名/获取点名名单"
    url = f"/service-profile/jst-app/attendances/members"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/查询老师在目前所教的班级")
def jst_app_teachers_teacherId_classes_get(teacherId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/首页/查询老师在目前所教的班级"
    url = f"/service-profile/jst-app/teachers/{teacherId}/classes"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页/查询老师在某个时间段内的排课计划")
def jst_app_teachers_teacherId_timetables_queries_get(teacherId, params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/首页/查询老师在某个时间段内的排课计划"
    url = f"/service-profile/jst-app/teachers/{teacherId}/timetables/queries"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/待发送班帖列表查询")
def jst_app_excellent_notes_findUnpublishedNote_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/精品班帖/待发送班帖列表查询"
    url = f"/service-profile/jst-app/excellent-notes/findUnpublishedNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/已发送班帖列表")
def jst_app_excellent_notes_publishedNote_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/精品班帖/已发送班帖列表"
    url = f"/service-profile/jst-app/excellent-notes/publishedNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/已发送班帖查阅")
def jst_app_excellent_notes_readNum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/精品班帖/已发送班帖查阅"
    url = f"/service-profile/jst-app/excellent-notes/readNum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/班帖详情")
def jst_app_excellent_notes_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/精品班帖/班帖详情"
    url = f"/service-profile/jst-app/excellent-notes/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/精品班帖/编辑班帖")
def jst_app_excellent_notes_courseNoteId_publishNote_post(courseNoteId, params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/精品班帖/编辑班帖"
    url = f"/service-profile/jst-app/excellent-notes/{courseNoteId}/publishNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/发布作业")
def jst_app_homework_publishHomework_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/发布作业"
    url = f"/service-profile/jst-app/homework/publishHomework"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/作业列表")
def jst_app_homework_homeworkList_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/作业列表"
    url = f"/service-profile/jst-app/homework/homeworkList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/班级列表")
def jst_app_homework_myClasses_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/班级列表"
    url = f"/service-profile/jst-app/homework/myClasses"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/学生作业查阅情况")
def jst_app_homework_readStatusOfStudent_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/学生作业查阅情况"
    url = f"/service-profile/jst-app/homework/readStatusOfStudent"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/作业详情")
def jst_app_homework_homeworkDetails_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/作业详情"
    url = f"/service-profile/jst-app/homework/homeworkDetails"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/删除作业")
def jst_app_homework_delHomework_delete(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/删除作业"    
    url = f"/service-profile/jst-app/homework/delHomework"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/提交（或修改）点名数据")
def jst_app_attendances_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通APP/点名/提交（或修改）点名数据"
    url = f"/service-profile/jst-app/attendances"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通APP/点名/补点名")
def jst_app_attendances_supply_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通APP/点名/补点名"
    url = f"/service-profile/jst-app/attendances/supply"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/首页感叹号")
def jst_app_status_post(params=None, body=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/首页感叹号"
    url = f"/service-profile/jst-app/status"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App撤回作业")
def jst_app_homework_recall_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App撤回作业"
    url = f"/service-profile/jst-app/homework/recall"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通App/作业/获取班级与课次")
def jst_app_homework_classIndex_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    name = "极师通App/作业/获取班级与课次"
    url = f"/service-profile/jst-app/homework/classIndex"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, name=name, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

