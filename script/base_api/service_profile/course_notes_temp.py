
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("/班贴/班贴列表")
def course_notes_getNoteList_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/getNoteList"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("/班贴/班贴列表导出")
def course_notes_real_exportExcel_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/real/exportExcel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/组件查询")
def course_notes_component_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/component"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/组件启用修改")
def course_notes_changeEnable_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/changeEnable"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板筛选查询")
def course_notes_queryNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/queryNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/创建模板")
def course_notes_createNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/createNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板筛选查询")
def course_notes_queryNoteById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/queryNoteById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板启用停用")
def course_notes_rNoteEnable_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/rNoteEnable"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板编辑")
def course_notes_editNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/editNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板复制")
def course_notes_copyNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/copyNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板校区查询")
def course_notes_queryNoteCampus_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/queryNoteCampus"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/添加模板校区关联")
def course_notes_addNoteCampus_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/addNoteCampus"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/发布新班帖（存草稿）")
def course_notes_courseNoteId_newNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/{courseNoteId}/newNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/查看新班帖详情")
def course_notes_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/提醒学生查看班帖(新)")
def course_notes_classStickerId_remindNew_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/{classStickerId}/remindNew"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/班帖列表（已发布）")
def course_notes_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/班帖列表(未发布)")
def course_notes_findOrCreateNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/findOrCreateNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("APP/班帖/班帖列表")
def course_notes_stickerList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/stickerList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("APP/班帖/班级列表")
def course_notes_queryClassList_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/queryClassList"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/模板删除")
def course_notes_deleteNote_delete(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/deleteNote"
    res = RunMethod.run_request("DELETE", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/首页感叹号")
def course_notes_status_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/status"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/查看班帖详情")
def course_notes_courseNoteId_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/{courseNoteId}/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/提醒学生查看班帖")
def course_notes_courseNoteId_reminds_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/{courseNoteId}/reminds"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/班帖/发布班帖（存草稿）")
def course_notes_courseNoteId_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/{courseNoteId}"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/上课/极客币")
def course_notes_queryJKDeatil_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/queryJKDeatil"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学习报告/极客资料")
def course_notes_getGeekMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/getGeekMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学习报告/获取教材所有讲次")
def course_notes_listLectureIndexes_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/listLectureIndexes"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学习报告/下讲预习")
def course_notes_prepareLessonMaterials_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/prepareLessonMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学习报告/发布极客资料")
def course_notes_publishGeekMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/publishGeekMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学习报告/保存极客资料")
def course_notes_saveGeekMaterial_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/saveGeekMaterial"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通/学习报告/本讲辅导")
def course_notes_tutorialMaterials_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/tutorialMaterials"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("获取以上课的课次信息")
def course_notes_getTaughtClassSchedule_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/getTaughtClassSchedule"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通web/学习报告/预存课次信息")
def course_notes_preview_getTaughtClassSchedule_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/preview/getTaughtClassSchedule"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通web/学习报告/预存学习报告详情")
def course_notes_preview_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/preview/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极师通web/学习报告/发送预存学习报告")
def course_notes_courseNoteId_preview_newNote_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/course-notes/{courseNoteId}/preview/newNote"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

