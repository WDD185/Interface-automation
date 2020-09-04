# coding: utf-8

run_setting = {
    "host": "192.168.32.43:3000",
    # [ding_ding_url]
    "web_hook": "https://oapi.dingtalk.com/robot/send?access_token=a57807f226f62dfa680edafc9394354c16754c88d111312361f24fab3b36b690",
    "report_path": "data/report/jky_report.xls",
    "email": {
        "host": "smtp.exmail.qq.com",
        "port": 465,
        "from_adress": "huangqiang1@jiuaoedu.com",
        "password": "JhyC5M5rCtfBGsab",
        "to_adresses": ["mzx6010@dingtalk.com"]
    },
    "postgreSql": {
        "database": "edu-admin",
        "user": "dev",
        "password": "192.168.32.41",
        "port": "5432"
    },
    "headers": {
        "header1": """{"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json, text/plain, */*"}""",
        "header2": """{"Content-Type": "application/json;charset=UTF-8", "Authorization": "Bearer ${global_token}"}""",
        "header3": """{"Accept": "application/json, text/plain, */*"}""",
        "header4": """{"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json, text/plain, */*"}"""
    },
    "excel_setting": {
        "sys_name": "极运营",
        "module_name": "登录、教务管理、报名、财务管理、系统设置、报表、知识库",
        "api_data_path": "data/api/jky_api.xlsx",
        "request_data_path": "data/request_data/jky_request_data.xlsx",
        # "sheet_name": ["login","teach_manage","apply","financial_manage","system_setting","statistics_report","knowledge"]
        "sheet_name": ["login"]
    },
    "global_variable": {
        "global_school_area_id": 3015,
        "student_id": "5878455"
    }
}
