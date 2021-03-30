
from common.run_method import RunMethod
from script.common_config import host
from script.common_config import public_assert
import pytest
import allure


@allure.step("极运营/财务管理/对账/新增对账记录")
def finance_accountingRecord_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accountingRecord/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/对账/查询上一次对账日期")
def finance_accountingRecord_lastTime_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accountingRecord/lastTime"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/对账/查询对账信息")
def finance_accountingRecord_system_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accountingRecord/system"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/对账/查询对账记录")
def finance_accountingRecord_all_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accountingRecord/all"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/对账/编辑对账备注")
def finance_accountingRecord_remark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accountingRecord/remark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/充值/学生充值_减少")
def finance_students_recharge_reduce_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/students/recharge/reduce"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/充值/学生充值_增加")
def finance_students_recharge_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/students/recharge/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/充值/充值记录修改")
def finance_update_recharge_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/update/recharge"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("通用/极运营/财务/查询学生校区账户")
def finance_query_student_school_account_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/query/student/school/account"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/退电子钱包")
def finance_refund_studentAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/refund/studentAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转/新增结转")
def finance_return_carryover_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/return/carryover"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/查询可退费")
def finance_refund_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/refund/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/查询退余额记录")
def finance_query_refund_studentAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/query/refund/studentAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/新增退费")
def finance_return_refund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/return/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转/查询可结转")
def finance_carryover_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/carryover/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/充值/充值记录查询")
def finance_query_recharge_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/query/recharge"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/缴款/修改备注")
def finance_payin_modifyRemark_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/payin/modifyRemark"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/账户设置/账户查询")
def finance_accounts_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accounts/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/账户设置/编辑/查询账户")
def finance_accounts_queryById_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accounts/queryById"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/账户统计/区域账户统计")
def finance_area_accounts_count_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/area/accounts/count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/查询退费记录")
def finance_refund_queryRecord_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/refund/queryRecord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/账户设置/修改账户")
def finance_accounts_update_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accounts/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/收支流水/查询收支流水")
def finance_financialFlow_query_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/financialFlow/query"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转/查询结转记录")
def finance_carryover_queryRecord_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/carryover/queryRecord"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/缴款/新增缴款")
def finance_payin_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/payin/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/缴款/缴款信息查询")
def finance_payin_query_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/payin/query"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/账户统计/校区账户统计")
def finance_school_accounts_count_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/school/accounts/count"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/缴款/撤销缴款")
def finance_payin_delete_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/payin/delete"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/缴款确认/批量确认")
def finance_payin_confirm_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/payin/confirm"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/账户设置/新增账户")
def finance_accounts_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/accounts/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/缴款/查询缴款记录")
def finance_payin_record_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/payin/record"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/查询退费原因修改记录")
def finance_refundReasonLog_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/refundReasonLog"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/退费/修改退费原因")
def finance_edit_refundReason_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/edit/refundReason"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/公司设置/根据公司id查询校区")
def finance_geekCompAccount_getSchoolAreaByCompId_compId_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/geekCompAccount/getSchoolAreaByCompId/{compId}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/公司设置/查询所有公司及所在区域")
def finance_geekCompAccount_queryAllCompany_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/geekCompAccount/queryAllCompany"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/公司设置/根据ID查询公司")
def finance_geekCompAccount_queryGeekCompById_id_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/geekCompAccount/queryGeekCompById/{id}"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/公司设置/编辑")
def finance_geekCompAccount_updateGeekCompAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/geekCompAccount/updateGeekCompAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/公司设置/新建公司")
def finance_geekCompAccount_saveGeekCompAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/geekCompAccount/saveGeekCompAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("分账逻辑/公司设置/查询所有")
def finance_geekCompAccount_queryAll_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/geekCompAccount/queryAll"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额设置列表")
def finance_introduce_rule_list_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/rule/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额设置新增")
def finance_introduce_rule_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/rule/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额设置开关")
def finance_introduce_rule_switch_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/rule/switch"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额设置修改")
def finance_introduce_rule_update_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/rule/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额-确认处理")
def finance_introduce_record_deal_receive_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/record/deal/receive"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额-处理列表")
def finance_introduce_record_deal_receive_list_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/record/deal/receive/list"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/财务管理/充值记录/导出充值记录")
def finance_export_recharge_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/export/recharge"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍领取分摊财务补偿接口")
def finance_introduce_record_deal_receive_deal_records_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/record/deal/receive/deal-records"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退费操作")
def finance_apply_refund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/apply/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退费审批操作")
def finance_approve_refund_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/approve/refund"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/重新提交退费操作")
def finance_resubmit_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/resubmit"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退电子钱包记录")
def finance_query_returnAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/query/returnAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退电子钱包审批操作")
def finance_approveReturnAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/approveReturnAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/退电子钱包重新提交操作")
def finance_resubmitReturnAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/resubmitReturnAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/转费申请操作")
def finance_applyTransferAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/applyTransferAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/转费审批操作")
def finance_approveTransferAccount_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/approveTransferAccount"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/前台业务/结转申请操作")
def finance_apply_carryover_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/apply/carryover"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("金蝶退费回调接口")
def finance_callbackPayStatusToKingdee_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_profile/finance/callbackPayStatusToKingdee"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/校区/退费确认单下载")
def finance_return_confirmation_slip_download_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/return/confirmation-slip/download"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍金额-学员发放汇总")
def finance_introduce_record_deal_receive_list_collection_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/record/deal/receive/list-collection"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("转介绍历史记录处理接口")
def finance_introduce_record_deal_history_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_finance/finance/introduce/record/deal/history"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置新增")
def finance_targets_add_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/add"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置修改")
def finance_targets_update_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/update"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置删除")
def finance_targets_del_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/del"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置查询全部")
def finance_targets_queryAll_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/queryAll"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置设置默认")
def finance_targets_setDefault_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/setDefault"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置设置排序")
def finance_targets_updateOrderNums_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/updateOrderNums"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细新增")
def finance_targets_add_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/add/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细修改")
def finance_targets_update_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/update/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细删除")
def finance_targets_del_detail_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/del/detail"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细查询全部")
def finance_targets_query_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/query/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细导出")
def finance_targets_export_detail_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/export/detail"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细下载模板")
def finance_targets_import_downModel_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/import/downModel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营/系统设置/财务目标设置/财务目标设置明细导入模板")
def finance_targets_import_uploadModel_post(params=None, body=None, header=None,return_json=True, default_assert=True, **kwargs):
    url = host + "/service_public/finance/targets/import/uploadModel"
    res = RunMethod.run_request("POST", url, params=params, body=body, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP查询学生电子钱包")
def finance_query_student_school_account_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/finance/query/student/school/account"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP查询学生电子钱包详情")
def finance_query_student_account_info_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/finance/query/student/account/info"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res


@allure.step("极运营APP查询学生电子钱包汇总")
def finance_query_student_account_sum_get(params=None, header=None, return_json=True, default_assert=True, **kwargs):
    url = host + "/api_operation_app/finance/query/student/account/sum"
    res = RunMethod.run_request("GET", url, params=params, header=header, return_json=return_json, **kwargs)
    if return_json and default_assert:
        public_assert(res)    
    return res

